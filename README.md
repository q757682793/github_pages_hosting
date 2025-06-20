# GitHub Pages HTML Hosting Plugin for Dify

🚀 一个强大的Dify插件，能够将HTML内容自动托管到您的GitHub Pages仓库并提供公开访问链接。

## ✨ 功能特性

- 📝 **HTML内容托管** - 接收HTML内容并自动托管到您的GitHub Pages仓库
- 🌐 **GitHub Pages集成** - 自动使用您的 `{username}.github.io` 仓库
- 🔗 **唯一链接生成** - 使用唯一ID生成格式为 `https://{username}.github.io/{unique_id}.html` 的访问链接
- 🆔 **唯一标识符** - 每个文件都有唯一的ID，避免冲突
- 🛡️ **安全验证** - 完整的GitHub token验证机制
- ⚡ **快速部署** - 自动监控部署状态
- 🎯 **用户友好** - 详细的进度反馈和错误提示

## 📦 安装要求

- Python 3.9+
- Dify Plugin Framework
- GitHub个人访问令牌
- GitHub账户（用于创建 `{username}.github.io` 仓库）

## 🚀 快速开始

### 1. 获取GitHub访问令牌

访问 [GitHub Settings > Personal access tokens](https://github.com/settings/tokens) 创建新令牌，需要以下权限：
- `repo` - 完整仓库权限

### 2. 配置插件

在Dify中安装插件并配置GitHub访问令牌。

### 3. 使用示例

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>🌟 我的第一个托管页面</h1>
    <p>通过Dify插件轻松托管HTML内容到GitHub Pages！</p>
</body>
</html>
```

## 📋 参数说明

| 参数 | 类型 | 必需 | 说明 | 默认值 |
|------|------|------|------|--------|
| `html_content` | string | ✅ | 要托管的HTML内容 | - |
| `unique_id` | string | ❌ | 文件的自定义唯一标识符 | 自动生成（时间戳+UUID） |

## 🎯 输出结果

```json
{
  "pages_url": "https://username.github.io/1719123456_abc12345.html",
  "repository_url": "https://github.com/username/username.github.io",
  "file_path": "1719123456_abc12345.html",
  "unique_id": "1719123456_abc12345",
  "status": "deployed"
}
```

### 输出字段说明

- `pages_url`: 可直接访问的GitHub Pages URL
- `repository_url`: GitHub仓库地址
- `file_path`: HTML文件在仓库中的路径
- `unique_id`: 文件的唯一标识符
- `status`: 部署状态（`deployed` 或 `deploying`）

## 💡 使用场景

- 🎨 **快速原型展示** - 分享设计原型和概念验证
- 📊 **数据可视化** - 托管图表和仪表板
- 📋 **临时页面** - 创建会议纪要、活动页面
- 🎓 **教学演示** - 教育内容和教程展示
- 📝 **表单收集** - 简单的信息收集页面
- 🔗 **链接分享** - 为每个HTML内容生成唯一的分享链接

## 🏗️ 工作原理

1. **用户输入** - 提供HTML内容和可选的唯一ID
2. **仓库检查** - 检查或创建用户的 `{username}.github.io` 仓库
3. **文件上传** - 使用唯一ID作为文件名上传HTML内容
4. **Pages启用** - 确保GitHub Pages已启用并正确配置
5. **URL返回** - 返回格式为 `https://{username}.github.io/{unique_id}.html` 的访问地址

## 🛠️ 开发和测试

### 环境设置

```bash
# 克隆项目
git clone <repository-url>
cd dify_plugin

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# 安装依赖
pip install -r requirements.txt
```

### 运行测试

```bash
# 基础功能测试
python test_plugin.py

# 运行插件
python main.py
```

### 项目结构

```
dify_plugin/
├── provider/
│   ├── github_pages_hosting.yaml  # 提供者配置
│   └── github_pages_hosting.py    # 凭证验证
├── tools/
│   ├── html_to_pages.yaml        # 工具配置
│   └── html_to_pages.py          # 工具实现
├── utils/
│   ├── __init__.py
│   └── github_manager.py         # GitHub API管理器
├── working/
│   └── progress.md               # 开发进度记录
├── manifest.yaml                # 插件主配置
├── requirements.txt             # Python依赖
├── main.py                     # 插件入口
├── test_plugin.py             # 测试脚本
├── icon.svg                   # 插件图标
├── PRIVACY.md                # 隐私政策
├── USAGE_GUIDE.md           # 使用指南
└── README.md               # 项目文档
```

## 🔧 故障排除

### 常见错误

1. **Token权限不足** - 确保GitHub token具有`repo`权限
2. **仓库不存在** - 插件会自动创建 `{username}.github.io` 仓库
3. **部署超时** - GitHub Pages部署通常需要1-3分钟
4. **API限制** - 遵循GitHub API速率限制

### 调试技巧

- 使用 `test_plugin.py` 验证基础功能
- 检查GitHub仓库是否正确创建
- 查看插件返回的详细错误信息
- 验证HTML内容格式正确性

## 🔒 安全注意事项

- 🔐 **保护访问令牌** - 不要在代码中硬编码令牌
- 🔍 **内容审查** - 确保HTML内容不包含敏感信息
- 📊 **监控使用** - 注意GitHub的使用限制和配额
- 🔄 **定期维护** - 定期更新令牌和清理不需要的文件

## 📈 性能优化

- ⚡ 使用合理的超时设置
- 🎯 实现智能重试机制
- 📊 监控API调用频率
- 🗂️ 合理管理文件数量

## 🆔 唯一ID管理

插件使用时间戳+UUID的组合生成唯一ID，格式为：`{timestamp}_{uuid}`

示例：`1719123456_abc12345`

- `timestamp`: Unix时间戳，确保时间唯一性
- `uuid`: 8位UUID，确保同一时间的唯一性

这样可以确保每个托管的HTML文件都有唯一的访问地址，避免文件名冲突。

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个插件！

## 📄 许可证

MIT License - 详见LICENSE文件

## 📚 相关资源

- [Dify插件开发文档](https://docs.dify.ai/plugin-dev-zh/)
- [GitHub Pages文档](https://docs.github.com/en/pages)
- [GitHub API文档](https://docs.github.com/en/rest)

---

❤️ 由 [Dify Plugin Framework](https://github.com/langgenius/dify) 强力驱动
