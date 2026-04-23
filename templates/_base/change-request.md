# 变更申请单

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

---

## 一、变更基本信息

| 字段         | 内容                     |
| ------------ | ------------------------ |
| 变更编号     | {{change_id}}            |
| 变更标题     | {{change_title}}         |
| 申请人       | {{requester}}            |
| 申请日期     | {{request_date}}         |
| 变更类型     | {{change_type}}          |
| 优先级       | {{change_priority}}      |
| 涉及模块     | {{affected_modules}}     |
| 期望完成日期 | {{expected_completion}}  |

## 二、变更描述

- **变更原因**: {{change_reason}}
- **变更内容**: {{change_description}}
- **变更前状态**: {{current_state}}
- **变更后期望状态**: {{target_state}}

## 三、影响分析

**进度影响**: 是否影响里程碑 {{milestone_impact}}，预计延期 {{delay_days}} 天

**成本影响**: 预计增加 {{additional_mandays}} 人天，费用 {{additional_cost}}

**质量影响**: 回归测试 {{regression_needed}}，影响用例数 {{affected_testcases}}

**范围影响**: 新增需求 {{new_requirements}} 项，修改需求 {{modified_requirements}} 项

## 四、风险评估

| 风险编号 | 风险描述 | 可能性 | 影响程度 | 应对措施 |
| -------- | -------- | ------ | -------- | -------- |
| {{risk_1_id}} | {{risk_1_desc}} | {{risk_1_probability}} | {{risk_1_impact}} | {{risk_1_mitigation}} |
| {{risk_2_id}} | {{risk_2_desc}} | {{risk_2_probability}} | {{risk_2_impact}} | {{risk_2_mitigation}} |

## 五、审批意见区

| 审批角色   | 意见                   | 签字                   | 日期                   |
| ---------- | ---------------------- | ---------------------- | ---------------------- |
| 项目经理   | {{pm_opinion}}         | {{pm_signer}}          | {{pm_sign_date}}       |
| 技术负责人 | {{tech_lead_opinion}}  | {{tech_lead_signer}}   | {{tech_lead_sign_date}} |
| 客户方     | {{client_opinion}}     | {{client_signer}}      | {{client_sign_date}}   |

- **审批结果**: {{approval_result}}
- **附加条件**: {{approval_conditions}}

---

> 本变更申请由 {{author}} 于 {{create_date}} 提交。经各方签字确认后生效。
