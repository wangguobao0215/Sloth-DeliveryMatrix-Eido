# 业务需求文档 (BRD)

## 文档信息

| 字段     | 内容                     |
| -------- | ------------------------ |
| 文档编号 | {{document_id}}          |
| 项目名称 | {{project_name}}         |
| 版本号   | {{document_version}}     |
| 编写人   | {{author}}               |
| 编写日期 | {{create_date}}          |
| 审批人   | {{approver}}             |
| 审批日期 | {{approval_date}}        |

### 版本历史

| 版本   | 修改日期     | 修改人       | 修改内容         |
| ------ | ------------ | ------------ | ---------------- |
| {{ver_1}} | {{ver_1_date}} | {{ver_1_author}} | {{ver_1_desc}} |

---

## 一、项目背景

{{project_background}}

## 二、业务目标

{{#each business_objectives}}
- **目标 {{@index}}**: {{this.description}}
  - 衡量指标: {{this.metric}}
  - 目标值: {{this.target_value}}
{{/each}}

## 三、范围定义

### 3.1 项目范围内 (In-Scope)

{{#each in_scope_items}}
- {{this}}
{{/each}}

### 3.2 项目范围外 (Out-of-Scope)

{{#each out_scope_items}}
- {{this}}
{{/each}}

## 四、干系人分析

| 干系人       | 角色         | 关注点           | 影响程度 | 沟通方式     |
| ------------ | ------------ | ---------------- | -------- | ------------ |
| {{sh_1_name}} | {{sh_1_role}} | {{sh_1_concern}} | {{sh_1_impact}} | {{sh_1_comm}} |
| {{sh_2_name}} | {{sh_2_role}} | {{sh_2_concern}} | {{sh_2_impact}} | {{sh_2_comm}} |

## 五、业务流程

### 5.1 当前流程 (As-Is)

{{as_is_process}}

### 5.2 目标流程 (To-Be)

{{to_be_process}}

## 六、功能需求清单

| 需求编号 | 功能名称     | 优先级   | 描述             | 关联业务目标 |
| -------- | ------------ | -------- | ---------------- | ------------ |
| {{fr_1_id}} | {{fr_1_name}} | {{fr_1_priority}} | {{fr_1_desc}} | {{fr_1_objective}} |
| {{fr_2_id}} | {{fr_2_name}} | {{fr_2_priority}} | {{fr_2_desc}} | {{fr_2_objective}} |
| {{fr_3_id}} | {{fr_3_name}} | {{fr_3_priority}} | {{fr_3_desc}} | {{fr_3_objective}} |

## 七、非功能需求

- **性能要求**: {{nfr_performance}}
- **安全要求**: {{nfr_security}}
- **可用性要求**: {{nfr_availability}}
- **兼容性要求**: {{nfr_compatibility}}
- **可维护性要求**: {{nfr_maintainability}}

## 八、约束与假设

### 约束条件

{{#each constraints}}
- {{this}}
{{/each}}

### 假设前提

{{#each assumptions}}
- {{this}}
{{/each}}

## 九、验收标准

| 序号 | 验收项           | 验收标准           | 验证方法     |
| ---- | ---------------- | ------------------ | ------------ |
| {{ac_1_no}} | {{ac_1_item}} | {{ac_1_criteria}} | {{ac_1_method}} |
| {{ac_2_no}} | {{ac_2_item}} | {{ac_2_criteria}} | {{ac_2_method}} |
