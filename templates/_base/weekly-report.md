# 项目周报

| 字段       | 内容                        |
| ---------- | --------------------------- |
| 项目名称   | {{project_name}}            |
| 报告周期   | {{report_period_start}} ~ {{report_period_end}} |
| 项目经理   | {{pm_name}}                 |
| 报告日期   | {{report_date}}             |

---

## 一、本周进展

{{#each progress_highlights}}
- {{this}}
{{/each}}

## 二、关键指标

### 里程碑状态

| 里程碑         | 计划完成日期 | 当前状态 | 完成率   | 备注         |
| -------------- | ------------ | -------- | -------- | ------------ |
| {{milestone_1_name}} | {{milestone_1_due}} | {{milestone_1_status}} | {{milestone_1_pct}}% | {{milestone_1_note}} |
| {{milestone_2_name}} | {{milestone_2_due}} | {{milestone_2_status}} | {{milestone_2_pct}}% | {{milestone_2_note}} |
| {{milestone_3_name}} | {{milestone_3_due}} | {{milestone_3_status}} | {{milestone_3_pct}}% | {{milestone_3_note}} |

- **整体完成率**: {{overall_completion_pct}}%
- **进度偏差**: {{schedule_variance}}

## 三、问题与风险

| 编号 | 问题/风险描述    | 严重程度 | 责任人       | 当前状态 | 预计解决日期 |
| ---- | ---------------- | -------- | ------------ | -------- | ------------ |
| {{issue_1_id}} | {{issue_1_desc}} | {{issue_1_severity}} | {{issue_1_owner}} | {{issue_1_status}} | {{issue_1_due}} |
| {{issue_2_id}} | {{issue_2_desc}} | {{issue_2_severity}} | {{issue_2_owner}} | {{issue_2_status}} | {{issue_2_due}} |

## 四、下周计划

{{#each next_week_plans}}
- {{this}}
{{/each}}

## 五、需要协调的事项

{{#each escalation_items}}
- **{{this.title}}**: {{this.description}}（需要 {{this.target}} 协助，期望 {{this.deadline}} 前解决）
{{/each}}

---

> 本报告由 {{pm_name}} 于 {{report_date}} 编制。如有疑问请联系项目组。
