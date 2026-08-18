# TIA Portal Openness 系统文档

[GitHub](https://github.com/lybhb8/tia-portal-openness-docs) | [在线文档](https://tia-portal-openness-docs.readthedocs.io/)

---

## 项目简介

本项目是 **Siemens TIA Portal Openness** 的完整中文技术文档，涵盖 API 参考、使用指南、最佳实践及版本变更说明。文档基于西门子官方资料整理，采用 **Sphinx** 构建，支持 HTML、PDF 和 ePub 格式输出。

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
- linkify-it-py 2.0+

---

## 快速开始

### 环境准备

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

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

## 文档构建（Sphinx）

本项目使用 [Sphinx](https://www.sphinx-doc.org/) 文档生成器，配合 [myst-parser](https://myst-parser.readthedocs.io/) 支持 Markdown 格式的文档编写。

### Sphinx 配置

核心配置文件：`docs/conf.py`

| 配置项 | 值 | 说明 |
|--------|-----|------|
| `extensions` | myst_parser, sphinx.ext.* | 启用的 Sphinx 扩展 |
| `source_suffix` | .md, .txt, .rst | 支持的文档格式 |
| `myst_enable_extensions` | 14 项扩展 | myst-parser 功能开关 |
| `html_theme` | sphinx13 | HTML 主题 |
| `language` | zh_CN | 文档语言 |
| `latex_engine` | xelatex | PDF 构建引擎（支持中文） |

### myst-parser 扩展

启用的扩展功能包括：

| 扩展名 | 功能说明 |
|--------|----------|
| `amsmath` | LaTeX 数学公式渲染 |
| `attrs_inline` | 行内 HTML 属性 |
| `colon_fence` | 使用 `:::` 作为代码围栏 |
| `deflist` | 定义列表支持 |
| `dollarmath` | `$...$` 内联公式 |
| `fieldlist` | 字段列表支持 |
| `html_admonition` | HTML 提示块 |
| `html_image` | 内联 HTML 图片 |
| `linkify` | 自动链接 URL 和邮箱 |
| `replacements` | 文本替换 |
| `smartquotes` | 智能引号 |
| `strikethrough` | 删除线 |
| `substitution` | 文本替换 |
| `tasklist` | 任务列表支持 |

### 构建命令

```bash
# 构建 HTML 文档
make html
# 输出: _build/html/index.html

# 构建 PDF 文档（需要 LaTeX 环境）
make pdf
# 输出: _build/latex/*.pdf

# 构建 ePub 文档
make epub
# 输出: _build/epub/TIA_OPENNESS_系统手册.epub

# 清理构建产物
make clean

# 查看可用命令
make help
```

### Sphinx 构建流程

1. **解析文档** — myst-parser 将 Markdown 转换为 docutils 节点树
2. **交叉引用** — 解析内部链接 `#锚点` 和外部引用
3. **生成索引** — 创建术语表、索引和搜索数据
4. **渲染输出** — 根据目标格式（HTML/PDF/ePub）生成最终文档

### 构建输出

| 格式 | 输出目录 | 说明 |
|------|----------|------|
| HTML | `_build/html/` | 可在线浏览的完整文档 |
| PDF | `_build/latex/` | 使用 XeLaTeX 编译的 PDF |
| ePub | `_build/epub/` | 电子书格式 |

---

## 部署到 Read the Docs

本项目已配置 [Read the Docs](https://readthedocs.org/) 自动构建和部署。

### 配置说明

项目根目录的 `.readthedocs.yaml` 文件控制构建行为：

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

sphinx:
  configuration: conf.py

formats:
  - pdf
  - htmlzip

python:
  install:
    - requirements: requirements.txt
```

| 配置项 | 值 | 说明 |
|--------|-----|------|
| `version` | 2 | RTD 配置格式版本 |
| `build.os` | ubuntu-22.04 | 构建操作系统 |
| `build.tools.python` | 3.11 | Python 版本 |
| `sphinx.configuration` | conf.py | Sphinx 配置文件路径 |
| `formats` | pdf, htmlzip | 输出格式（PDF 和 ZIP 包） |
| `python.install` | requirements.txt | Python 依赖安装方式 |

### 自动部署流程

1. 推送代码到 GitHub master 分支
2. Read the Docs 自动检测到 `.readthedocs.yaml` 配置
3. 自动安装依赖并构建文档
4. 构建完成后发布到 `https://tia-portal-openness-docs.readthedocs.io/`

### 本地预览

```bash
# 使用 Python 内置 HTTP 服务器预览
python -m http.server 8000 --directory _build/html

# 访问 http://localhost:8000
```

---

## 项目结构

```
TIA openness/
├── README.md                 # 项目说明
├── LICENSE                   # 许可证
├── requirements.txt          # Python 依赖
├── Makefile                  # 构建脚本
├── .readthedocs.yaml         # Read the Docs 配置
├── .gitignore                # Git 忽略规则
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
│   ├── _static/              # 静态资源（CSS、JS、图片）
│   ├── _templates/           # 自定义模板
│   ├── _themes/              # Sphinx 主题
│   └── images/               # 文档图片
└── _build/                   # 构建输出（不提交）
    ├── html/
    ├── latex/
    └── epub/
```

---

## 文档规范

### 编写规范

1. **Markdown 格式**：使用标准 Markdown + myst-parser 扩展
2. **代码块**：使用正确的语言标识（`csharp`、`xml`、`python` 等）
3. **内部链接**：使用 `#锚点` 格式，锚点由标题自动生成
4. **图片**：使用相对路径引用
5. **章节命名**：使用 `XX 标题.md` 格式

### 锚点规则

myst-parser 根据标题自动生成锚点：

| 标题示例 | 生成的锚点 |
|----------|------------|
| `### 5.2.8 连接到 TIA Portal` | `#528-连接到-tia-portal` |
| `## 快速开始` | `#快速开始` |
| `# 第一章` | `#第一章` |

**链接格式**：`[链接文本](#锚点)` 或 `[链接文本](#528-连接到-tia-portal)`

### 代码块规范

```markdown
这是说明文字。

```csharp
// 代码示例
var project = portal.GetCurrentProcess();
```

这是后续说明。
```

**注意**：代码块前后需要空行，否则可能导致渲染错误。

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

### 提交前检查

```bash
# 安装依赖
pip install -r requirements.txt

# 构建文档（确保无警告）
make html

# 检查构建输出
cat _build/html/index.html
```

### 文档规范

- 使用 Markdown 格式编写
- 代码块使用正确的语言标识
- 内部链接使用正确的锚点格式
- 图片使用相对路径引用

---

## 许可证

本仓库文档基于西门子官方文档整理，仅供学习参考。

---

## 相关链接

- [西门子 TIA Portal Openness 官方文档](https://www.siemens.com)
- [Sphinx 官方文档](https://www.sphinx-doc.org/)
- [myst-parser 文档](https://myst-parser.readthedocs.io/)
- [Read the Docs 文档](https://docs.readthedocs.io/)
- [GitHub 仓库](https://github.com/lybhb8/tia-portal-openness-docs)
