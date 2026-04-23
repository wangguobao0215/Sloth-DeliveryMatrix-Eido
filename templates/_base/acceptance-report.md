# 项目验收报告

| 字段     | 内容                     |
| -------- | ------------------------ |
| 项目名称 | {{project_name}}         |
| 委托方   | {{client_name}}          |
| 验收日期 | {{acceptance_date}}      |
| 文档版本 | {{document_version}}     |

---

## 一、项目概述

{{project_overview}}

- **项目编号**: {{project_code}}
- **合同编号**: {{contract_no}}
- **项目周期**: {{project_start}} ~ {{project_end}}

## 二、验收范围

{{#each acceptance_scope}}
- {{this}}
{{/each}}

## 三、验收标准与结果

| 序号 | 验收项           | 验收标准           | 验收方法   | 结果   | 备注         |
| ---- | ---------------- | ------------------ | ---------- | ------ | ------------ |
| {{item_1_no}} | {{item_1_name}} | {{item_1_criteria}} | {{item_1_method}} | {{item_1_result}} | {{item_1_note}} |
| {{item_2_no}} | {{item_2_name}} | {{item_2_criteria}} | {{item_2_method}} | {{item_2_result}} | {{item_2_note}} |
| {{item_3_no}} | {{item_3_name}} | {{item_3_criteria}} | {{item_3_method}} | {{item_3_result}} | {{item_3_note}} |

- **验收通过率**: {{pass_rate}}%

## 四、遗留问题

| 编号 | 问题描述         | 严重程度 | 处理方案       | 预计解决日期 |
| ---- | ---------------- | -------- | -------------- | ------------ |
| {{issue_1_id}} | {{issue_1_desc}} | {{issue_1_severity}} | {{issue_1_plan}} | {{issue_1_due}} |

## 五、培训情况

- **培训日期**: {{training_date}}
- **培训内容**: {{training_content}}
- **参训人员**: {{training_attendees}}
- **培训效果**: {{training_result}}

## 六、结论与建议

### 验收结论

{{acceptance_conclusion}}

### 改进建议

{{#each improvement_suggestions}}
- {{this}}
{{/each}}

## 七、签字确认

| 角色       | 姓名           | 签字   | 日期           |
| ---------- | -------------- | ------ | -------------- |
| 甲方代表   | {{client_rep}} |        | {{sign_date}}  |
| 乙方代表   | {{vendor_rep}} |        | {{sign_date}}  |
| 项目经理   | {{pm_name}}    |        | {{sign_date}}  |
