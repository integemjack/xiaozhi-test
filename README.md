# xiaozhi-test

自动化测试项目，用于验证 [xiaozhi_v18](https://creator.integem.com/wp-content/soft/xiaozhi_v18.zip) 项目中所有脚本的正确性。

## 测试内容

GitHub Actions 工作流会自动下载远程项目压缩包并执行以下测试：

### Linux 环境测试
- **YAML 文件验证** - 检查所有 `.yml` / `.yaml` 文件的语法
- **Docker Compose 验证** - 验证 docker-compose 文件是否合法
- **Shell 脚本语法检查** - 使用 `bash -n` 检查 `.sh` / `.command` 文件
- **Batch 脚本基础验证** - 检查 `.bat` 文件是否包含有效命令
- **Python 脚本语法检查** - 使用 `py_compile` 编译检查
- **Dockerfile 检查** - 使用 hadolint 进行 lint
- **文件权限和换行符检查** - 确保 shell 脚本有执行权限，无 CRLF 问题

### Windows 环境测试
- **Batch 脚本验证** - 在原生 Windows 环境下验证 `.bat` 文件
- **YAML 文件验证** - 同上
- **Python 脚本语法检查** - 同上
- **Docker Compose 验证** - 同上

## 触发方式

- Push 到 `main` 或 `master` 分支
- Pull Request 到 `main` 或 `master` 分支
- 手动触发 (workflow_dispatch)

## 远程项目来源

- ZIP 下载地址: https://creator.integem.com/wp-content/soft/xiaozhi_v18.zip
- GitHub 仓库: https://github.com/integemjack/xiaozhi-test.git
