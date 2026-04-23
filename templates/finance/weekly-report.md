# 金融项目周报

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{report_date}}            |
| 文档版本 | {{document_version}}       |

| 报告周期 | {{report_period_start}} ~ {{report_period_end}} |
| -------- | ------------------------------------------------ |
| 项目经理 | {{pm_name}}                                      |
| 密级     | {{classification_level}}                         |

---

## 一、本周进展

{{#each progress_highlights}}
- {{this}}
{{/each}}

## 二、里程碑状态

| 里程碑       | 计划完成日期 | 当前状态 | 完成率   | 备注         |
| ------------ | ------------ | -------- | -------- | ------------ |
| {{milestone_1_name}} | {{milestone_1_due}} | {{milestone_1_status}} | {{milestone_1_pct}}% | {{milestone_1_note}} |
| {{milestone_2_name}} | {{milestone_2_due}} | {{milestone_2_status}} | {{milestone_2_pct}}% | {{milestone_2_note}} |

- **整体完成率**: {{overall_completion_pct}}%
- **进度偏差**: {{schedule_variance}}

## 三、合规检查点

| 检查项       | 状态     | 责任人       | 备注         |
| ------------ | -------- | ------------ | ------------ |
| {{comp_1_item}} | {{comp_1_status}} | {{comp_1_owner}} | {{comp_1_note}} |
| {{comp_2_item}} | {{comp_2_status}} | {{comp_2_owner}} | {{comp_2_note}} |

## 四、安全事件记录

| 事件编号 | 事件描述         | 等级     | 处理状态 | 责任人       |
| -------- | ---------------- | -------- | -------- | ------------ |
| {{sec_1_id}} | {{sec_1_desc}} | {{sec_1_level}} | {{sec_1_status}} | {{sec_1_owner}} |

## 五、数据脱敏状态

| 数据类型     | 脱敏方式     | 覆盖率   | 合规状态 |
| ------------ | ------------ | -------- | -------- |
| {{mask_1_type}} | {{mask_1_method}} | {{mask_1_coverage}}% | {{mask_1_status}} |
| {{mask_2_type}} | {{mask_2_method}} | {{mask_2_coverage}}% | {{mask_2_status}} |

## 六、等保相关进展

- **等保等级**: {{mlps_level}}
- **本周完成项**: {{mlps_completed_items}}
- **待整改项**: {{mlps_pending_items}}
- **下一步计划**: {{mlps_next_steps}}

## 七、审计追踪记录

| 审计事项     | 审计人       | 状态     | 发现问题     | 整改期限     |
| ------------ | ------------ | -------- | ------------ | ------------ |
| {{audit_1_item}} | {{audit_1_auditor}} | {{audit_1_status}} | {{audit_1_finding}} | {{audit_1_due}} |

## 八、问题与风险

| 编号 | 问题/风险描述    | 严重程度 | 责任人       | 当前状态 | 预计解决日期 |
| ---- | ---------------- | -------- | ------------ | -------- | ------------ |
| {{issue_1_id}} | {{issue_1_desc}} | {{issue_1_severity}} | {{issue_1_owner}} | {{issue_1_status}} | {{issue_1_due}} |

## 九、下周计划

{{#each next_week_plans}}
- {{this}}
{{/each}}

---

> 本报告由 {{author}} 于 {{report_date}} 编制。本文档涉及金融敏感信息，请按密级要求妥善保管。
