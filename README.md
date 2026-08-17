# TIA Portal Openness Documentation

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
docs/
├── chapter_01_1 网络安全信息.md
├── chapter_02_2 TIA Portal Openness 自述文件.md
├── chapter_03_3 TIA Portal Openness 中的新功能.md
├── chapter_04_4 基本知识.md
├── chapter_05_5 TIA Portal Openness API.md
├── chapter_06_6 导出导入.md
├── chapter_07_7 主要变化.md
└── images/ (1087 张图片)
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

#### Documentation Structure

```
docs/
├── chapter_01_1 Cybersecurity Information.md
├── chapter_02_2 TIA Portal Openness Readme.md
├── chapter_03_3 New Features in TIA Portal Openness.md
├── chapter_04_4 Basic Knowledge.md
├── chapter_05_5 TIA Portal Openness API.md
├── chapter_06_6 Export Import.md
├── chapter_07_7 Major Changes.md
└── images/ (1087 images)
```

#### Contributing

Issues and Pull Requests are welcome!

#### License

Documentation based on Siemens official documentation, for learning reference only.
