# Sprint 评审报告

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

| Sprint   | {{sprint_number}}                     |
| -------- | ------------------------------------- |
| 迭代周期 | {{sprint_start}} ~ {{sprint_end}}     |
| 评审日期 | {{review_date}}                       |
| 参会人员 | {{attendees}}                         |

---

## 一、Sprint 目标完成情况

- **Sprint 目标**: {{sprint_goal}}
- **是否达成**: {{goal_achieved}}
- **达成说明**: {{goal_summary}}

## 二、Demo 清单

| 序号 | 功能/特性        | 演示人       | 演示状态 | 利益相关者反馈   |
| ---- | ---------------- | ------------ | -------- | ---------------- |
| {{demo_1_seq}} | {{demo_1_feature}} | {{demo_1_presenter}} | {{demo_1_status}} | {{demo_1_feedback}} |
| {{demo_2_seq}} | {{demo_2_feature}} | {{demo_2_presenter}} | {{demo_2_status}} | {{demo_2_feedback}} |

## 三、Story 完成率

| 分类         | 数量     | Story Points |
| ------------ | -------- | ------------ |
| 已完成       | {{done_count}} | {{done_points}} |
| 未完成       | {{undone_count}} | {{undone_points}} |
| 新增(Scope变更) | {{added_count}} | {{added_points}} |
| **合计**     | {{total_count}} | {{total_points}} |

- **完成率**: {{completion_rate}}%
- **Scope 变更率**: {{scope_change_rate}}%

## 四、速度趋势

| Sprint       | 计划 Points | 完成 Points | Velocity |
| ------------ | ----------- | ----------- | -------- |
| {{prev_2_sprint}} | {{prev_2_planned}} | {{prev_2_done}} | {{prev_2_velocity}} |
| {{prev_1_sprint}} | {{prev_1_planned}} | {{prev_1_done}} | {{prev_1_velocity}} |
| {{current_sprint}} | {{current_planned}} | {{current_done}} | {{current_velocity}} |

- **趋势分析**: {{velocity_trend_analysis}}

## 五、产品待办变更

{{#each backlog_changes}}
- {{this}}
{{/each}}

## 六、利益相关者反馈

{{#each stakeholder_feedback}}
- **{{this.name}}**: {{this.comment}}
{{/each}}

## 七、下个 Sprint 规划

- **Sprint 目标**: {{next_sprint_goal}}
- **计划 Story Points**: {{next_sprint_points}}
- **关键交付物**: {{next_sprint_deliverables}}
- **已知风险**: {{next_sprint_risks}}

---

> 本报告由 {{author}} 于 {{create_date}} 编制。
