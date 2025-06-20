from collections.abc import Generator
from typing import Any
import time

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

# 导入GitHub管理器
from utils.github_manager import GitHubPagesManager


class HtmlToPagesTool(Tool):
    """将HTML内容托管到GitHub Pages的工具"""
    
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        执行HTML到GitHub Pages的托管过程
        
        Args:
            tool_parameters: 工具参数字典
            
        Yields:
            ToolInvokeMessage: 工具执行消息
        """
        try:
            # 获取必需参数
            html_content = tool_parameters.get("html_content", "").strip()
            
            # 验证HTML内容
            if not html_content:
                yield self.create_text_message("错误：HTML内容不能为空")
                return
            
            # 获取可选参数 - 现在只需要一个唯一ID来生成文件名
            unique_id = tool_parameters.get("unique_id")
            if not unique_id:
                # 生成唯一ID（时间戳 + UUID）
                import uuid
                unique_id = f"{int(time.time())}_{str(uuid.uuid4())[:8]}"
            
            # 使用唯一ID作为文件名
            file_name = f"{unique_id}.html"
            repository_description = "GitHub Pages hosting for user content"
            
            # 获取GitHub token
            github_token = self.runtime.credentials.get("github_token")
            if not github_token:
                yield self.create_text_message("错误：GitHub访问令牌未配置")
                return
            
            yield self.create_text_message("🚀 开始处理HTML内容...")
            
            # 初始化GitHub管理器
            github_manager = GitHubPagesManager(github_token)
            
            # 验证HTML内容
            if not github_manager.validate_html_content(html_content):
                yield self.create_text_message("⚠️ 警告：提供的内容可能不是有效的HTML格式")
            
            # 获取用户信息
            yield self.create_text_message("📝 获取GitHub用户信息...")
            user_info = github_manager.get_user_info()
            username = user_info["login"]
            
            # 使用用户的GitHub Pages仓库 {username}.github.io
            repository_name = f"{username}.github.io"
            yield self.create_text_message(f"� 目标仓库: {repository_name}")
            
            # 确保GitHub Pages仓库存在
            yield self.create_text_message(f"📁 检查或创建GitHub Pages仓库...")
            repo_info = github_manager.ensure_pages_repository(username)
            
            repository_url = repo_info["html_url"]
            yield self.create_text_message(f"✅ GitHub Pages仓库已准备: {repository_url}")
            
            # 上传HTML文件到GitHub Pages仓库
            yield self.create_text_message(f"📤 上传HTML文件: {file_name}")
            upload_result = github_manager.upload_file(
                owner=username,
                repo=repository_name,
                file_path=file_name,
                content=html_content,
                message=f"Add {file_name} via Dify plugin"
            )
            
            yield self.create_text_message("✅ HTML文件上传成功")
            
            # 确保GitHub Pages已启用（对于用户的GitHub Pages仓库）
            yield self.create_text_message("🌐 确保GitHub Pages已启用...")
            try:
                github_manager.ensure_pages_enabled(username, repository_name)
            except Exception as e:
                yield self.create_text_message(f"⚠️ GitHub Pages配置: {str(e)}")
            
            # 构建Pages URL - 直接使用用户的GitHub Pages域名
            pages_url = f"https://{username}.github.io/{unique_id}.html"
            
            yield self.create_text_message("⏳ GitHub Pages部署中...")
            
            # 等待部署完成（GitHub Pages仓库通常部署较快）
            deployment_success = github_manager.wait_for_pages_deployment(username, repository_name, max_wait=60)
            
            if deployment_success:
                yield self.create_text_message("🎉 GitHub Pages部署成功！")
                status = "deployed"
            else:
                yield self.create_text_message("⏰ GitHub Pages正在部署中，通常几分钟内完成")
                status = "deploying"
            
            # 返回结果
            result = {
                "pages_url": pages_url,
                "repository_url": repository_url,
                "file_path": file_name,
                "unique_id": unique_id,
                "status": status
            }
            
            yield self.create_json_message(result)
            
            # 为工作流提供变量
            yield self.create_variable_message("pages_url", pages_url)
            yield self.create_variable_message("repository_url", repository_url)
            yield self.create_variable_message("unique_id", unique_id)
            yield self.create_variable_message("status", status)
            
            # 用户友好的最终消息
            yield self.create_text_message(f"""
🌟 HTML内容已成功托管到您的GitHub Pages！

� 访问地址: {pages_url}
📁 仓库地址: {repository_url}
📄 文件名: {file_name}
🔖 唯一ID: {unique_id}
📊 状态: {status}

💡 提示: 内容已上传到您的 {username}.github.io 仓库，通常几分钟内即可访问。
""")
            
        except Exception as e:
            error_message = f"❌ 处理过程中发生错误: {str(e)}"
            yield self.create_text_message(error_message)
            
            # 提供故障排除建议
            if "rate limit" in str(e).lower():
                yield self.create_text_message("💡 建议: GitHub API速率限制，请稍后重试")
            elif "token" in str(e).lower():
                yield self.create_text_message("💡 建议: 请检查GitHub访问令牌是否有效且具有正确权限")
            elif "repository" in str(e).lower():
                yield self.create_text_message("💡 建议: 仓库名称可能已存在或包含无效字符")
            else:
                yield self.create_text_message("💡 建议: 请检查网络连接和GitHub服务状态")
