# 3 TIA Portal Openness 中的新功能

TIA Portal Openness V19 中具备以下新功能与创新。有关各个主题的更多详细信息，请参见产品文档的相关章节。
- 常规
- 无论使用哪个 API 版本，均导入任何受支持的 SimaticML 版本。
- SimaticML 导入更加灵活，包含项目语言处理选项。
- 项目
- 组态在虚拟 PLC 中使用 S7-1500 块

## - 硬件配置

- 创建、读取、更新和删除传送区以进行PLC-PLC直接数据交换。
- 管理 PLC 系统记录组态。
- 管理 CPU 固件 3.1 的新 PLC 访问控制组态（UMAC 和访问级别）。
- 更改采用 PLC 多语言支持的 OPC UA 报警和事件的默认语言。
- 在所有重载的“SetAttributes”方法中以正确的顺序批量更改硬件参数

## - 硬件模块

- 最新支持对以下模块进行参数访问：ET200pro Safety、ET200eco PN Safety、ET200MP Safety。
- 扩展了对 SCALANCE XC-200（V4.3 及以上版本）、XP-200（V4.3 及以上版本）、SC-600（V2.3 及以上版本）的参数访问。

## - CAx 数据交换

- 通过 AutomationML 导入/导出 CAx 数据，并通过 API（而不是日志文件）检索结果。
- 支持硬件配置交换的附加属性。

## - 在线场景

- 获得可访问的在线设备以进行下载或上传。
- 将 PLC（含 Safety）下载到 SIMATIC 存储卡文件夹。
- 处理 UMAC 用户管理数据，进行下载。
- 为在线 PLC 访问合法性提供 UMAC 凭据。

## - PLC 用户程序

- 对数据块中的附加列进行读取和写入访问。
- 程序块上关于支持虚拟 PLC 的信息性属性。
- 扩展 SimaticML 方案，以支持使用命名值类型。
- 块导出/导入期间支持命名值常量。

## - 安全工程组态

- 在“安全管理编辑器”(Safety Administration Editor)中组态序列号，对F-PLC进行唯一标识。

## - UMAC

- 为项目用户组态别名。

## - 工艺对象

- 支持工艺对象组。
- 为解析器程序导入和导出文件

## - Startdrive

- 将工艺对象连接至 Startdrive 报文。
- 读取 Startdrive 报文的硬件 ID。
- 支持新 Startdrive 设备。
- 第三方编码器的参数设置。
- WinCC Unified
- 访问附加的对象属性和运行系统设置。
- Test Suite Advanced
- 针对系统测试组态 OPC UA 设置。
- 针对应用测试组态模式。
- 支持主副本。
• Version Control Interface (VC)
- VCI 设置用于在 SimaticML 导入期间处理非活动项目语言。
- 将 VCI 对象状态初始化到映射文件。
- 报警和 ProDiag
- 在 PLC 组态中管理系统诊断。
- Web 服务器
- 在 CPU 固件版本 V3.1 中管理对 Web 服务器的数据访问。
TIA Portal Openness V16 中的主要更改 (页 1868)
TIA Portal Openness V17 中有关长期稳定性的主要更改 (页 1863)
TIA Portal Openness V19 中有关长期稳定性的主要更改 (页 34)
TIA Portal Openness V15.1 中的主要更改 (页 1870)
TIA Portal Openness V15 中的主要更改 (页 1873)
V14 SP1 中的主要变更 (页 1876)
V14 中的主要变更 (页 1914)
