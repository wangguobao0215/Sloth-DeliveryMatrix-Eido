# 项目状态更新邮件

**主题**: 【{{project_name}}】项目周进展更新 — {{report_period}}

---

{{client_greeting}}，

感谢您持续关注{{project_name}}项目。以下是本周项目进展概要：

## 项目进度概要

- **整体进度**: {{overall_progress}}%
- **当前阶段**: {{current_phase}}
- **进度状态**: {{schedule_status}}

## 关键成果

{{#each key_achievements}}
- {{this}}
{{/each}}

## 待解决事项

{{#each pending_items}}
- **{{this.title}}**: {{this.description}}（预计 {{this.eta}} 解决）
{{/each}}

## 下阶段计划

{{#each next_phase_plans}}
- {{this}}
{{/each}}

---

如有任何疑问或需要进一步沟通，请随时联系我。

此致

{{pm_name}}
{{pm_title}}
{{pm_contact}}
