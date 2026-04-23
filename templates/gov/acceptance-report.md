# 项目验收报告

**（政府/国企正式验收文档）**

| 字段     | 内容                       |
| -------- | -------------------------- |
| 文档编号 | {{document_id}}            |
| 甲方     | {{party_a_name}}           |
| 乙方     | {{party_b_name}}           |
| 验收日期 | {{acceptance_date}}        |

---

## 一、项目概况

- **项目名称**: {{project_name}}
- **合同编号**: {{contract_no}}
- **项目周期**: {{project_start}} ~ {{project_end}}
- **项目概述**: {{project_overview}}

## 二、验收依据

本次验收依据以下文件和标准进行：

### 2.1 合同文件

{{#each contract_references}}
- {{this}}
{{/each}}

### 2.2 技术标准

{{#each technical_standards}}
- {{this}}
{{/each}}

### 2.3 项目文档

{{#each project_documents}}
- {{this}}
{{/each}}

## 三、验收内容与标准

| 序号 | 验收类别     | 验收内容         | 验收标准           | 验证方法   | 结果   |
| ---- | ------------ | ---------------- | ------------------ | ---------- | ------ |
| {{vc_1_no}} | {{vc_1_cat}} | {{vc_1_content}} | {{vc_1_criteria}} | {{vc_1_method}} | {{vc_1_result}} |
| {{vc_2_no}} | {{vc_2_cat}} | {{vc_2_content}} | {{vc_2_criteria}} | {{vc_2_method}} | {{vc_2_result}} |
| {{vc_3_no}} | {{vc_3_cat}} | {{vc_3_content}} | {{vc_3_criteria}} | {{vc_3_method}} | {{vc_3_result}} |

## 四、验收过程记录

### 4.1 验收时间

{{acceptance_period}}

### 4.2 验收方式

{{acceptance_method}}

### 4.3 验收参与人员

| 姓名         | 单位         | 职务         | 角色         |
| ------------ | ------------ | ------------ | ------------ |
| {{ap_1_name}} | {{ap_1_org}} | {{ap_1_title}} | {{ap_1_role}} |
| {{ap_2_name}} | {{ap_2_org}} | {{ap_2_title}} | {{ap_2_role}} |

### 4.4 验收过程说明

{{acceptance_process_desc}}

## 五、验收结果

- **功能验收**: {{func_acceptance_result}}
- **性能验收**: {{perf_acceptance_result}}
- **文档验收**: {{doc_acceptance_result}}
- **培训验收**: {{train_acceptance_result}}
- **综合评价**: {{overall_assessment}}

## 六、遗留问题处理方案

| 编号 | 问题描述         | 严重程度 | 处理方案       | 责任方   | 完成期限     |
| ---- | ---------------- | -------- | -------------- | -------- | ------------ |
| {{ri_1_id}} | {{ri_1_desc}} | {{ri_1_severity}} | {{ri_1_plan}} | {{ri_1_owner}} | {{ri_1_due}} |

## 七、验收结论

{{acceptance_conclusion}}

---

## 签字页

| 角色         | 姓名           | 单位             | 签字   | 日期           |
| ------------ | -------------- | ---------------- | ------ | -------------- |
| 甲方代表     | {{party_a_rep}} | {{party_a_name}} |        | {{sign_date}}  |
| 乙方代表     | {{party_b_rep}} | {{party_b_name}} |        | {{sign_date}}  |

**甲方（盖章）**:                          **乙方（盖章）**:

日期:                                       日期:
