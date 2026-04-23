# 项目周报（呈报）

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{report_date}}            |
| 文档版本 | {{document_version}}       |

| 呈报单位 | {{report_org}}                                   |
| -------- | ------------------------------------------------ |
| 报告周期 | {{report_period_start}} ~ {{report_period_end}}  |
| 密级     | {{classification_level}}                         |
| 文号     | {{document_number}}                              |

---

**{{report_to_org}} ：**

现将 {{project_name}} 项目本周工作进展情况呈报如下：

## 一、本周工作完成情况

{{#each progress_items}}
（{{this.seq}}）{{this.content}}
{{/each}}

## 二、里程碑进展

| 里程碑名称   | 计划完成日期 | 实际进度 | 完成状态 | 说明         |
| ------------ | ------------ | -------- | -------- | ------------ |
| {{milestone_1_name}} | {{milestone_1_due}} | {{milestone_1_pct}}% | {{milestone_1_status}} | {{milestone_1_note}} |
| {{milestone_2_name}} | {{milestone_2_due}} | {{milestone_2_pct}}% | {{milestone_2_status}} | {{milestone_2_note}} |
| {{milestone_3_name}} | {{milestone_3_due}} | {{milestone_3_pct}}% | {{milestone_3_status}} | {{milestone_3_note}} |

综合以上各项里程碑，项目整体完成率为 {{overall_completion_pct}}%，进度偏差为 {{schedule_variance}}。

## 三、存在问题及处理措施

| 序号 | 问题描述         | 严重程度 | 责任单位     | 处理措施       | 预计解决日期 |
| ---- | ---------------- | -------- | ------------ | -------------- | ------------ |
| {{issue_1_seq}} | {{issue_1_desc}} | {{issue_1_severity}} | {{issue_1_org}} | {{issue_1_action}} | {{issue_1_due}} |
| {{issue_2_seq}} | {{issue_2_desc}} | {{issue_2_severity}} | {{issue_2_org}} | {{issue_2_action}} | {{issue_2_due}} |

## 四、需协调解决的事项

{{#each escalation_items}}
（{{this.seq}}）{{this.description}}（需请 {{this.target_org}} 协助，恳请于 {{this.deadline}} 前予以支持）
{{/each}}

## 五、下周工作计划

{{#each next_week_plans}}
（{{this.seq}}）{{this.content}}
{{/each}}

## 六、其他需汇报事项

{{other_notes}}

---

特此呈报。

呈报单位：{{report_org}}（盖章） | 项目负责人：{{pm_name}} | 联系电话：{{pm_phone}} | {{report_date}}

**盖章区**

| 审核     | 批准         |
| -------- | ------------ |
| 审核人：{{reviewer}} | 批准人：{{approver}} |
| 日期：{{review_date}} | 日期：{{approve_date}} |

---

> 本周报由 {{author}} 于 {{report_date}} 编制，按照政府信息化项目管理要求呈报。
