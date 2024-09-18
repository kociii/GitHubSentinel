# GitHub Sentinel

GitHub Sentinel 是一款开源的交互式工具，专为开发者和项目管理人员设计，旨在提高团队协作效率和项目管理的便捷性。

## 功能

- **交互式命令行界面**：提供了一系列命令来管理 GitHub 仓库订阅。
- **命令支持**：
  - ：添加仓库订阅
  - ：移除仓库订阅
  - ：获取所有订阅仓库的更新
  - ：列出所有订阅的仓库
  - ：退出 shell
- **定时任务调度**：使用 APScheduler 实现后台定时任务，不阻塞用户操作。

## 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/你的用户名/github-sentinel.git
   cd github-sentinel
   ```

2. 创建并激活虚拟环境（可选）：

   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上是
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用

1. 运行 启动交互式 shell：

   ```bash
   python sentinel.py
   ```

2. 使用 或 列出可用命令及其描述。

## 贡献

欢迎贡献代码！请查看 [Contributing Guidelines](链接到贡献指南) 以获取更多信息。

## 许可证

此项目采用 MIT 许可证。详情请参阅 [LICENSE](链接到许可证文件)。
