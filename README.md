# TIA Portal Openness 系统文档

[中文文档](#t porta-openness-文档) | [English Docs](#tia-portal-openness-documentation)

---

## 中文版

### TIA Portal Openness 文档

这是 Siemens TIA Portal Openness 的完整中文技术文档，包含 API 参考、使用说明和最佳实践。

#### 内容概览

- **第 1 章** 网络安全信息
- **第 2 章** TIA Portal Openness 自述文件
- **第 3 章** TIA Portal Openness 中的新功能
- **第 4 章** 基本知识
- **第 5 章** TIA Portal Openness API（核心参考）
- **第 6 章** 导出/导入
- **第 7 章** 主要变化

#### 系统要求

- TIA Portal V16 或更高版本
- Windows 10/11
- .NET Framework 4.8 或更高版本

#### 快速开始

```csharp
using Siemens.Engineering;
using Siemens.Engineering.Hmi;

// 连接到 TIA Portal
var portal = Engineering.Create("TIA Portal");

// 获取当前项目
var project = portal.GetCurrentProcess();
```

#### 文档结构

```
TIA openness/
├── README.md
├── LICENSE
├── conf.py
├── Makefile
├── requirements.txt
├── .readthedocs.yaml
├── docs/
│   ├── index.md
│   ├── chapter_*.md (7 个章节)
│   └── images/ (1087 张图片)
└── tests/
    ├── README.md
    ├── test_build.py
    ├── test_content.py
    ├── test_links.py
    ├── test_examples.py
    └── requirements-test.txt
```

#### 本地测试

```bash
# 运行所有测试
make test

# 或单独运行
python tests/test_build.py
python tests/test_content.py
python tests/test_links.py
python tests/test_examples.py
```

#### 贡献

欢迎提交 Issue 和 Pull Request！

#### 许可证

本仓库文档基于西门子官方文档整理，仅供学习参考。

---

## English Version

### TIA Portal Openness Documentation

Complete Chinese technical documentation for Siemens TIA Portal Openness, including API reference, usage guides, and best practices.

#### Contents

- **Chapter 1** Cybersecurity Information
- **Chapter 2** TIA Portal Openness Readme
- **Chapter 3** New Features in TIA Portal Openness
- **Chapter 4** Basic Knowledge
- **Chapter 5** TIA Portal Openness API (Core Reference)
- **Chapter 6** Export/Import
- **Chapter 7** Major Changes

#### System Requirements

- TIA Portal V16 or higher
- Windows 10/11
- .NET Framework 4.8 or higher

#### Quick Start

```csharp
using Siemens.Engineering;
using Siemens.Engineering.Hmi;

// Connect to TIA Portal
var portal = Engineering.Create("TIA Portal");

// Get current project
var project = portal.GetCurrentProcess();
```

#### 文档结构

```
TIA openness/
├── README.md
├── LICENSE
├── conf.py
├── Makefile
├── requirements.txt
├── .readthedocs.yaml
├── docs/
│   ├── index.md
│   ├── chapter_*.md (7 chapters)
│   └── images/ (1087 images)
└── tests/
    ├── README.md
    ├── test_build.py
    ├── test_content.py
    ├── test_links.py
    ├── test_examples.py
    └── requirements-test.txt
```

#### Local Testing

```bash
# Run all tests
make test

# Or run individually
python tests/test_build.py
python tests/test_content.py
python tests/test_links.py
python tests/test_examples.py
```

#### Contributing

Issues and Pull Requests are welcome!

#### License

Documentation based on Siemens official documentation, for learning reference only.
