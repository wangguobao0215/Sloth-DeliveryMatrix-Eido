# 测试报告

**（参照 GB/T 15532-2008）**

| 字段     | 内容                       |
| -------- | -------------------------- |
| 文档编号 | {{document_id}}            |
| 密级     | {{classification_level}}   |
| 项目名称 | {{project_name}}           |
| 版本号   | {{document_version}}       |
| 编制单位 | {{authoring_org}}          |
| 编制日期 | {{create_date}}            |

---

## 1 测试概述

### 1.1 测试目的

{{test_purpose}}

### 1.2 测试范围

{{test_scope}}

### 1.3 测试依据

{{#each test_references}}
- {{this}}
{{/each}}

### 1.4 测试类型

{{#each test_types}}
- {{this}}
{{/each}}

## 2 测试环境

### 2.1 硬件环境

| 设备类型     | 规格配置         | 数量   | 用途       |
| ------------ | ---------------- | ------ | ---------- |
| {{hw_1_type}} | {{hw_1_spec}} | {{hw_1_qty}} | {{hw_1_usage}} |

### 2.2 软件环境

| 软件名称     | 版本号       | 用途         |
| ------------ | ------------ | ------------ |
| {{sw_1_name}} | {{sw_1_ver}} | {{sw_1_usage}} |

### 2.3 测试工具

| 工具名称     | 版本号       | 用途         |
| ------------ | ------------ | ------------ |
| {{tool_1_name}} | {{tool_1_ver}} | {{tool_1_usage}} |

## 3 测试用例执行情况

### 3.1 执行摘要

| 测试类型     | 用例总数 | 通过   | 失败   | 阻塞   | 未执行 | 通过率   |
| ------------ | -------- | ------ | ------ | ------ | ------ | -------- |
| {{type_1_name}} | {{type_1_total}} | {{type_1_pass}} | {{type_1_fail}} | {{type_1_block}} | {{type_1_skip}} | {{type_1_rate}}% |
| {{type_2_name}} | {{type_2_total}} | {{type_2_pass}} | {{type_2_fail}} | {{type_2_block}} | {{type_2_skip}} | {{type_2_rate}}% |
| **合计**     | {{total_cases}} | {{total_pass}} | {{total_fail}} | {{total_block}} | {{total_skip}} | {{total_rate}}% |

### 3.2 关键测试用例结果

| 用例编号 | 用例名称     | 测试结果 | 备注         |
| -------- | ------------ | -------- | ------------ |
| {{tc_1_id}} | {{tc_1_name}} | {{tc_1_result}} | {{tc_1_note}} |

## 4 缺陷统计

### 4.1 按严重程度分布

| 严重程度 | 数量   | 已修复 | 未修复 | 延期处理 |
| -------- | ------ | ------ | ------ | -------- |
| 致命     | {{sev_critical_total}} | {{sev_critical_fixed}} | {{sev_critical_open}} | {{sev_critical_deferred}} |
| 严重     | {{sev_major_total}} | {{sev_major_fixed}} | {{sev_major_open}} | {{sev_major_deferred}} |
| 一般     | {{sev_normal_total}} | {{sev_normal_fixed}} | {{sev_normal_open}} | {{sev_normal_deferred}} |
| 轻微     | {{sev_minor_total}} | {{sev_minor_fixed}} | {{sev_minor_open}} | {{sev_minor_deferred}} |

### 4.2 按状态分布

| 状态     | 数量         |
| -------- | ------------ |
| 新建     | {{status_new}} |
| 已修复   | {{status_fixed}} |
| 已验证   | {{status_verified}} |
| 已关闭   | {{status_closed}} |
| 延期     | {{status_deferred}} |

## 5 测试结论

{{test_conclusion}}

- **质量评估**: {{quality_assessment}}
- **是否达到测试出口标准**: {{exit_criteria_met}}
- **建议**: {{test_recommendation}}

## 6 遗留问题

| 编号 | 问题描述         | 严重程度 | 处理建议       | 预计解决版本 |
| ---- | ---------------- | -------- | -------------- | ------------ |
| {{rem_1_id}} | {{rem_1_desc}} | {{rem_1_severity}} | {{rem_1_plan}} | {{rem_1_version}} |

---

> 本报告依据 GB/T 15532-2008《计算机软件测试规范》编制。
