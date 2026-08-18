# TIA Portal Openness 系统文档

[GitHub](https://github.com/lybhb8/tia-portal-openness-docs) | [在线文档](https://tia-portal-openness-docs.readthedocs.io/)

---

## 项目简介

本项目是 **Siemens TIA Portal Openness** 的完整中文技术文档，涵盖 API 参考、使用指南、最佳实践及版本变更说明。文档基于西门子官方资料整理，采用 **Sphinx** 构建，支持 HTML 和 PDF 格式输出。

TIA Portal Openness 是西门子为 TIA Portal（博途）平台提供的自动化编程接口，允许开发者通过 .NET 应用程序控制和扩展 TIA Portal 的功能，实现工程数据的批量处理、自动化配置和集成开发。

---

## 文档目录

| 章节 | 内容描述 |
|------|----------|
| [第 1 章](docs/01%20网络安全信息.md) | 网络安全信息 |
| [第 2 章](docs/02%20TIA%20Portal%20Openness%20自述文件.md) | TIA Portal Openness 自述文件 |
| [第 3 章](docs/03%20TIA%20Portal%20Openness%20中的新功能.md) | TIA Portal Openness 中的新功能 |
| [第 4 章](docs/04%20基本知识.md) | 基本知识 |
| [第 5 章](docs/05%20TIA%20Portal%20Openness%20API.md) | TIA Portal Openness API（核心参考） |
| [第 6 章](docs/06%20导出导入.md) | 导出/导入 |
| [第 7 章](docs/07%20主要变化.md) | 主要变化 |

---

## 系统要求

### 运行环境
- TIA Portal V16 或更高版本
- Windows 10/11 (64-bit)
- .NET Framework 4.8 或更高版本 / .NET 6+

### 文档构建环境
- Python 3.10+
- Sphinx 7.0+
- myst-parser 2.0+

---

## 快速开始

### C# 代码示例

```csharp
using Siemens.Engineering;
using Siemens.Engineering.Hmi;

// 连接到 TIA Portal
var portal = Engineering.Create("TIA Portal");

// 获取当前项目
var project = portal.GetCurrentProcess();

// 访问设备
foreach (var device in project.ConnectedDevices)
{
    Console.WriteLine($"设备: {device.Name}");
}
```

---

## 构建文档

### 安装依赖

```bash
# 创建虚拟环境
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

### 构建命令

```bash
# 构建 HTML 文档
make html

# 构建 PDF 文档
make pdf

# 清理构建产物
make clean

# 查看所有可用命令
make help
```

### 在线预览

```bash
# 本地启动开发服务器（支持热重载）
make watch

# 或使用 HTTP 服务器查看已构建的文档
make serve
```

---

## 部署到 Read the Docs

本项目已配置 [Read the Docs](https://readthedocs.org/) 自动构建和部署。

### 配置说明

项目根目录的 `.readthedocs.yaml` 文件控制构建行为：

| 配置项 | 值 | 说明 |
|--------|-----|------|
| `version` | 2 | RTD 配置格式版本 |
| `build.os` | ubuntu-22.04 | 构建操作系统 |
| `build.tools.python` | 3.11 | Python 版本 |
| `sphinx.configuration` | conf.py | Sphinx 配置文件路径 |
| `formats` | pdf, htmlzip | 输出格式（HTML/PDF/EPUB） |
| `python.install` | requirements.txt | Python 依赖安装方式 |

### 自动部署流程

1. 推送代码到 GitHub master 分支
2. Read the Docs 自动检测到 `.readthedocs.yaml` 配置
3. 自动安装依赖并构建文档
4. 构建完成后发布到 `https://tia-portal-openness-docs.readthedocs.io/`

### 手动构建所有格式

```bash
# 构建 HTML
make html

# 构建 PDF（需要 LaTeX 环境）
make pdf

# 构建 ePub
make epub
```

---

## 项目结构

```
TIA openness/
├── README.md                 # 项目说明
├── LICENSE                   # 许可证
├── requirements.txt          # Python 依赖
├── pyproject.toml            # 项目配置
├── Makefile                  # 构建脚本
├── .readthedocs.yaml         # Read the Docs 配置
├── docs/
│   ├── index.md              # 文档首页
│   ├── 01 网络安全信息.md
│   ├── 02 TIA Portal Openness 自述文件.md
│   ├── 03 TIA Portal Openness 中的新功能.md
│   ├── 04 基本知识.md
│   ├── 05 TIA Portal Openness API.md
│   ├── 06 导出导入.md
│   ├── 07 主要变化.md
│   ├── conf.py               # Sphinx 配置
│   ├── Makefile              # Sphinx 构建脚本
│   ├── _static/              # 静态资源（CSS、JS、图片）
│   ├── _templates/           # 自定义模板
│   ├── _themes/              # Sphinx 主题
│   └── images/               # 文档图片（1000+）
└── tests/                    # 测试脚本
    ├── test_build.py
    ├── test_content.py
    ├── test_links.py
    └── test_examples.py
```

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

### 提交前检查

```bash
# 构建文档（确保无警告）
make html

# 运行测试
make test
```

### 文档规范

- 使用 Markdown 格式编写
- 代码块使用正确的语言标识（如 `csharp`、`xml`）
- 内部链接使用正确的锚点格式：`[链接文本](#锚点)`
- 图片使用相对路径引用

---

## 许可证

本仓库文档基于西门子官方文档整理，仅供学习参考。

---

## 相关链接

- [西门子 TIA Portal Openness 官方文档](https://www.siemens.com)
- [Sphinx 官方文档](https://www.sphinx-doc.org/)
- [Read the Docs](https://readthedocs.org/)
- [GitHub 仓库](https://github.com/lybhb8/tia-portal-openness-docs)
