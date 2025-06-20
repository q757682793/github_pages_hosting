# GitHub Pages HTML托管插件 - 使用指南

## 📖 概述

这个Dify插件可以将HTML内容自动托管到您的GitHub Pages仓库（`{username}.github.io`），为每个HTML文件生成唯一的访问链接。非常适合快速分享HTML演示、静态页面或临时网站。

## 🚀 快速开始

### 1. 获取GitHub访问令牌

1. 访问 [GitHub Personal Access Tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token" > "Generate new token (classic)"
3. 设置令牌名称，如 "Dify HTML Hosting Plugin"
4. 选择以下权限：
   - ✅ `repo` - 完整仓库权限
5. 点击 "Generate token" 并复制生成的令牌

⚠️ **重要**: 令牌只显示一次，请妥善保存！

### 2. 配置插件

1. 在Dify中添加此插件
2. 在插件设置中输入你的GitHub访问令牌
3. 保存配置

### 3. 使用插件

基本使用示例：

```html
<!DOCTYPE html>
<html>
<head>
    <title>我的测试页面</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>这是通过Dify插件托管的HTML页面。</p>
</body>
</html>
```

## 🛠️ 功能详解

### 输入参数

| 参数名 | 类型 | 必需 | 说明 | 默认值 |
|--------|------|------|------|--------|
| `html_content` | string | ✅ | 要托管的HTML内容 | - |
| `unique_id` | string | ❌ | 自定义唯一标识符 | 自动生成 |

### 输出结果

```json
{
  "pages_url": "https://username.github.io/1719123456_abc12345.html",
  "repository_url": "https://github.com/username/username.github.io",
  "file_path": "1719123456_abc12345.html",
  "unique_id": "1719123456_abc12345",
  "status": "deployed"
}
```

### 🔗 URL格式

所有托管的HTML文件都遵循以下URL格式：

```
https://{username}.github.io/{unique_id}.html
```

- `{username}`: 您的GitHub用户名
- `{unique_id}`: 文件的唯一标识符

例如：如果您的GitHub用户名是 `test`，唯一ID是 `1719123456_abc12345`，则访问地址为：
```
https://test.github.io/1719123456_abc12345.html
```

## 📝 使用场景示例

### 1. 简单网页分享

```html
<!DOCTYPE html>
<html>
<head>
    <title>项目演示</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 我的项目演示</h1>
        <p>这是一个简单的项目演示页面。</p>
        <ul>
            <li>功能A：描述</li>
            <li>功能B：描述</li>
            <li>功能C：描述</li>
        </ul>
    </div>
</body>
</html>
```

### 2. 数据展示页面

```html
<!DOCTYPE html>
<html>
<head>
    <title>数据报告</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>📊 月度销售报告</h1>
    <canvas id="salesChart" width="400" height="200"></canvas>
    
    <script>
        const ctx = document.getElementById('salesChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['一月', '二月', '三月', '四月'],
                datasets: [{
                    label: '销售额',
                    data: [12, 19, 3, 5],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            }
        });
    </script>
</body>
</html>
```

### 3. 表单收集页面

```html
<!DOCTYPE html>
<html>
<head>
    <title>问卷调查</title>
    <style>
        .form-container { max-width: 500px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, textarea { width: 100%; padding: 8px; border: 1px solid #ccc; }
        button { background: #007cba; color: white; padding: 10px 20px; border: none; }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>📋 用户反馈表</h1>
        <form>
            <div class="form-group">
                <label for="name">姓名：</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">邮箱：</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="feedback">反馈：</label>
                <textarea id="feedback" name="feedback" rows="4" required></textarea>
            </div>
            <button type="submit">提交反馈</button>
        </form>
    </div>
</body>
</html>
```

## 🎯 最佳实践

### 1. HTML内容优化

- ✅ 使用完整的HTML文档结构
- ✅ 包含适当的`<title>`标签
- ✅ 使用响应式设计
- ✅ 优化图片和资源加载
- ❌ 避免过大的内联资源

### 2. 唯一ID管理

- 🔄 让系统自动生成ID以确保唯一性
- 📝 记录重要页面的唯一ID以便后续访问
- 🗂️ 考虑使用有意义的自定义ID（仅在确定不冲突时）

### 3. 内容组织

- 📁 相关页面可以使用相似的ID前缀
- 🏷️ 在HTML中添加元数据标签
- 📅 包含创建日期等信息

## 🔧 故障排除

### 常见问题

**Q: 为什么我的页面无法访问？**
A: 
- 检查GitHub Pages是否已启用
- 确认部署状态（首次部署需要1-3分钟）
- 验证URL格式是否正确

**Q: 如何更新已托管的页面？**
A: 
- 使用相同的`unique_id`重新调用插件
- 系统会自动覆盖原有文件

**Q: 可以托管多少个页面？**
A: 
- GitHub Pages没有明确的文件数量限制
- 建议合理使用，定期清理不需要的文件

**Q: 支持哪些HTML功能？**
A: 
- ✅ 标准HTML、CSS、JavaScript
- ✅ 外部资源引用（CDN等）
- ❌ 服务器端处理（PHP、Python等）
- ❌ 数据库连接

### 错误代码

| 错误类型 | 可能原因 | 解决方案 |
|----------|----------|----------|
| Token无效 | GitHub令牌过期或权限不足 | 重新生成令牌并确认权限 |
| 仓库创建失败 | 仓库名冲突或权限问题 | 检查仓库是否已存在 |
| 文件上传失败 | 网络问题或文件过大 | 检查网络连接，减小文件大小 |
| Pages配置失败 | 仓库设置问题 | 手动检查GitHub Pages设置 |

## 🔒 安全指南

### 敏感信息处理

- 🚫 **永远不要**在HTML中包含密码、API密钥等敏感信息
- 🔍 上传前仔细检查内容
- 🌐 记住GitHub Pages是公开的，任何人都可以访问

### 最佳安全实践

- 🔐 定期轮换GitHub访问令牌
- 📊 监控仓库的访问情况
- 🗑️ 及时删除不需要的文件
- 🔄 使用短期的临时页面

## 📊 使用统计

您可以通过以下方式查看页面访问情况：

1. **GitHub Insights**: 在仓库页面查看流量统计
2. **Google Analytics**: 在HTML中添加GA代码
3. **第三方工具**: 使用其他网站分析工具

## 🤝 获取帮助

如果遇到问题：

1. 查看本文档的故障排除部分
2. 检查GitHub状态页面
3. 查看Dify插件日志
4. 联系插件维护者

## 📚 相关资源

- [GitHub Pages官方文档](https://docs.github.com/en/pages)
- [HTML基础教程](https://developer.mozilla.org/zh-CN/docs/Web/HTML)
- [CSS样式指南](https://developer.mozilla.org/zh-CN/docs/Web/CSS)
- [JavaScript基础](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
