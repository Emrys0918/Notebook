# Notebook 上传到 GitHub 指南（快速对照版）

本指南帮助你把 `/data/xjq/notebook` 里的内容（如 Jupyter notebooks、Markdown、图片等）稳定地推送到 GitHub 仓库 `Emrys0918/Notebook`。

---

## 一、一次性准备（首次配置）

1) 配置 Git 身份（全局，只需一次）
```bash
git config --global user.name "你的名字或昵称"
git config --global user.email "你的邮箱"
```

2) 准备并添加 SSH 公钥到 GitHub（推荐用 SSH 推送，更稳）
- 查看公钥（复制整段）：
```bash
cat ~/.ssh/id_rsa.pub
```
- 在 GitHub: Settings → SSH and GPG keys → New SSH key → 粘贴保存。
- 验证连接（期望看到 "Hi <username>! You've successfully authenticated" 字样）：
```bash
ssh -T git@github.com
```
若提示主机指纹问题，可先加入指纹：
```bash
ssh-keyscan -H github.com >> ~/.ssh/known_hosts
```

3) 设置远端为 SSH（只需一次）
- 如果还没设置：
```bash
git -C /data/xjq/notebook remote add origin git@github.com:Emrys0918/Notebook.git
```
- 如果之前是 HTTPS，改为 SSH：
```bash
git -C /data/xjq/notebook remote set-url origin git@github.com:Emrys0918/Notebook.git
```

---

## 二、常用忽略（.gitignore）
已在仓库中添加了常用忽略规则，包括：
- Python 缓存与构建：`__pycache__/`、`*.pyc`、`build/`、`dist/`、`*.egg-info/` 等
- Jupyter：`.ipynb_checkpoints/`、`.jupyter/`
- 工具缓存：`.pytest_cache/`、`.mypy_cache/`、`.ruff_cache/`、`.tox/` 等
- 编辑器/IDE：`.vscode/`、`.idea/`
- OS：`.DS_Store`、`Thumbs.db`
- 以及忽略子仓库备份：`pytorch_notebook/.git.bak/`

如需新增忽略，直接在仓库根目录编辑 `.gitignore` 并提交。

---

## 三、避免子仓库冲突（嵌套 .git）
如果某个子目录本身是一个 Git 仓库（里面有 `.git` 目录），会导致父仓库 `git add` 报错。解决：
```bash
# 以 pytorch_notebook 为例（把内部 .git 改名备份）
mv /data/xjq/notebook/pytorch_notebook/.git /data/xjq/notebook/pytorch_notebook/.git.bak
# 确保 .gitignore 已忽略 .git.bak 目录
```
这样父仓库就能正常跟踪子目录的文件内容。

---

## 四、每次上传步骤（日常使用）
在仓库根目录 `/data/xjq/notebook`：
```bash
# 1. 查看状态（了解有哪些变更）
git status

# 2. 选择性或全部加入暂存区（二选一）
# 选择性：
git add 路径A 路径B
# 全部：
git add -A

# 3. 提交（写上清晰的提交信息）
git commit -m "说明这次改了什么"

# 4. 推送到远端（首次会建立跟踪关系）
git push -u origin master
# 后续只需：
git push
```

可选验证：
```bash
git remote -v      # 查看远端
git branch -vv     # 查看本地分支与上游跟踪情况
```

---

## 五、常见问题排查
- 问：`gnutls_handshake() failed`（HTTPS TLS 错误）
  - 解：改用 SSH 远端：`git remote set-url origin git@github.com:Emrys0918/Notebook.git`

- 问：`Permission denied (publickey)`（SSH 无权限）
  - 解：将 `~/.ssh/id_rsa.pub` 添加到 GitHub；再 `ssh -T git@github.com` 验证。

- 问：推送被拒，因为单文件 > 100MB
  - 解：避免提交超大文件；必要时使用 Git LFS（需要另行安装与配置）。

- 问：不小心把某文件加入了暂存区，想撤回
  - 解：`git reset HEAD <文件>`

- 问：想撤销最近一次提交（未推送）
  - 解：`git reset --soft HEAD~1`（保留改动，撤销提交）；或 `git reset --hard HEAD~1`（连改动也撤销，谨慎！）

---

## 六、附录：新建仓库（如需）
如果是全新目录要变成 Git 仓库：
```bash
cd /data/xjq/notebook
# 1) 初始化
git init
# 2) 设置远端（推荐 SSH）
git remote add origin git@github.com:Emrys0918/Notebook.git
# 3) 首次提交与推送
git add -A
git commit -m "init"
git push -u origin master
```


如果你不需要保留 Git 历史：

## 1. 删除 .git 目录
```bash
rm -rf .git
```

## 2. 重新初始化

```bash
git init
```
## 3. 确保 .gitignore 正确配置（添加 data/ 等大文件目录）
```bash
echo "data/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

## 4. 提交
```bash
git add -A
git commit -m "Initial commit"
```

## 5. 推送到远程
```bash
git remote add origin https://github.com/Emrys0918/LLM.git
git push -u origin master --force
```
