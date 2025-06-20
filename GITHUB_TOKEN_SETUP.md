# GitHub Token权限问题解决方案

## 问题诊断

当您看到错误 "Resource not accessible by personal access token" 时，这意味着您的GitHub token没有足够的权限来访问Contents API。

## 解决方案

### 方案1：使用经典Personal Access Token（推荐）

1. 访问 [GitHub Settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
2. 点击 "Generate new token" > "Generate new token (classic)"
3. 设置令牌名称，如 "Dify HTML Hosting Plugin"
4. 选择过期时间（建议30-90天）
5. **重要**：在权限部分勾选：
   - ✅ `repo` - 完整仓库权限（这包括读写公开和私有仓库）
6. 点击 "Generate token" 并复制令牌
7. 在Dify插件设置中使用新的令牌

### 方案2：使用Fine-grained Personal Access Token

如果您想使用更细粒度的权限控制：

1. 访问 [GitHub Settings > Personal access tokens > Fine-grained tokens](https://github.com/settings/personal-access-tokens/new)
2. 设置令牌基本信息
3. 在 "Repository access" 中选择：
   - "Selected repositories" 然后选择您的 `{username}.github.io` 仓库
   - 或者选择 "All repositories"（不推荐）
4. 在 "Repository permissions" 中设置：
   - ✅ `Contents`: **Read and write**
   - ✅ `Pages`: **Write**（可选，用于Pages配置）
   - ✅ `Metadata`: **Read**（基本信息访问）
5. 生成并使用新令牌

## 验证权限

使用以下命令验证您的token权限：

```bash
curl -H "Authorization: token YOUR_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/user

# 检查响应头中的 X-OAuth-Scopes 字段
```

对于Contents API权限测试：

```bash
curl -H "Authorization: token YOUR_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/YOUR_USERNAME/YOUR_USERNAME.github.io
```

## 常见问题

**Q: 我使用的是经典token，勾选了repo权限，为什么还是403？**
A: 请确认：
- 令牌没有过期
- 仓库确实存在
- 您有该仓库的访问权限

**Q: Fine-grained token应该选择什么权限？**
A: 最小必需权限：
- Contents: Read and write
- Metadata: Read

**Q: 可以使用组织的仓库吗？**
A: 可以，但需要确保token有访问组织仓库的权限，并且您在组织中有相应的权限。

## 推荐配置

对于此插件，推荐使用**经典Personal Access Token**，因为：
1. 配置简单，只需勾选 `repo` 权限
2. 兼容性更好
3. 权限覆盖更全面

---

如果按照以上步骤操作后仍有问题，请检查：
1. GitHub服务状态
2. 网络连接
3. 令牌是否正确复制（无多余空格）
