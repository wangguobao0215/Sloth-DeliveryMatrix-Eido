# 测试报告

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

---

## 一、文档信息

| 版本   | 修改日期     | 修改人       | 审核人       | 修改说明         |
| ------ | ------------ | ------------ | ------------ | ---------------- |
| {{ver_1}} | {{ver_1_date}} | {{ver_1_author}} | {{ver_1_reviewer}} | {{ver_1_desc}} |

## 二、测试概述

- **测试目的**: {{test_purpose}}
- **测试策略**: {{test_strategy}}

## 三、测试范围

{{#each test_scope_items}}
- {{this}}
{{/each}}

## 四、测试环境

| 类别     | 配置信息          | 版本/规格     | 备注         |
| -------- | ----------------- | ------------- | ------------ |
| 服务器   | {{server_config}} | {{server_spec}} | {{server_note}} |
| 数据库   | {{db_config}}     | {{db_spec}}   | {{db_note}}  |
| 测试工具 | {{tool_config}}   | {{tool_spec}} | {{tool_note}} |

## 五、测试执行统计

| 测试类型 | 用例总数 | 通过 | 失败 | 阻塞 | 未执行 | 通过率 |
| -------- | -------- | ---- | ---- | ---- | ------ | ------ |
| {{type_1_name}} | {{type_1_total}} | {{type_1_pass}} | {{type_1_fail}} | {{type_1_block}} | {{type_1_skip}} | {{type_1_rate}}% |
| {{type_2_name}} | {{type_2_total}} | {{type_2_pass}} | {{type_2_fail}} | {{type_2_block}} | {{type_2_skip}} | {{type_2_rate}}% |
| **合计** | {{total_cases}} | {{total_pass}} | {{total_fail}} | {{total_block}} | {{total_skip}} | {{total_rate}}% |

## 六、缺陷分析

| 严重程度 | 数量 | 已修复 | 未修复 | 延期处理 |
| -------- | ---- | ------ | ------ | -------- |
| 致命     | {{sev_critical_total}} | {{sev_critical_fixed}} | {{sev_critical_open}} | {{sev_critical_deferred}} |
| 严重     | {{sev_major_total}} | {{sev_major_fixed}} | {{sev_major_open}} | {{sev_major_deferred}} |
| 一般     | {{sev_normal_total}} | {{sev_normal_fixed}} | {{sev_normal_open}} | {{sev_normal_deferred}} |
| 轻微     | {{sev_minor_total}} | {{sev_minor_fixed}} | {{sev_minor_open}} | {{sev_minor_deferred}} |

## 七、测试结论

{{test_conclusion}}

- **质量评估**: {{quality_assessment}}
- **是否达到出口标准**: {{exit_criteria_met}}

## 八、遗留问题

| 编号 | 问题描述 | 严重程度 | 处理建议 | 预计解决时间 |
| ---- | -------- | -------- | -------- | ------------ |
| {{rem_1_id}} | {{rem_1_desc}} | {{rem_1_severity}} | {{rem_1_plan}} | {{rem_1_due}} |

## 九、建议

{{#each recommendations}}
- {{this}}
{{/each}}

---

> 本报告由 {{author}} 于 {{create_date}} 编制。如有疑问请联系测试组。
