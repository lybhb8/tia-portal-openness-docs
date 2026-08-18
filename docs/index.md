# TIA Portal Openness 系统文档

```{toctree}
:caption: 目录
:maxdepth: 2

1 网络安全信息.md
2 TIA Portal Openness 自述文件.md
3 TIA Portal Openness 中的新功能.md
4 基本知识.md
5 TIA Portal Openness API.md
6 导出导入.md
7 主要变化.md
```

## 快速开始 (C#)

```csharp
using Siemens.Engineering;

var portal = Engineering.Create("TIA Portal");
var project = portal.GetCurrentProcess();
```

## 文档导航

| 章节 | 描述 |
|------|------|
| 第 1 章 | 网络安全信息 |
| 第 2 章 | 自述文件 |
| 第 3 章 | 新功能 |
| 第 4 章 | 基本知识 |
| 第 5 章 | API 参考 |
| 第 6 章 | 导出/导入 |
| 第 7 章 | 主要变化 |
