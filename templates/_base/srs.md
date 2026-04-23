# 软件需求规格说明书

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

---

## 一、文档信息表

| 版本   | 修改日期     | 修改人       | 审核人       | 修改说明         |
| ------ | ------------ | ------------ | ------------ | ---------------- |
| {{ver_1}} | {{ver_1_date}} | {{ver_1_author}} | {{ver_1_reviewer}} | {{ver_1_desc}} |

## 二、引言

- **编写目的**: {{purpose}}
- **项目背景**: {{project_background}}

| 术语       | 定义                     |
| ---------- | ------------------------ |
| {{term_1}} | {{term_1_def}}           |
| {{term_2}} | {{term_2_def}}           |

## 三、总体描述

- **产品愿景**: {{product_vision}}
- **用户特征**: {{user_characteristics}}
- **硬件环境**: {{hardware_env}}
- **软件环境**: {{software_env}}
- **网络环境**: {{network_env}}

## 四、功能需求

| 需求编号 | 功能名称 | 优先级 | 描述 | 输入 | 输出 | 前置条件 |
| -------- | -------- | ------ | ---- | ---- | ---- | -------- |
| {{func_req_1_id}} | {{func_req_1_name}} | {{func_req_1_priority}} | {{func_req_1_desc}} | {{func_req_1_input}} | {{func_req_1_output}} | {{func_req_1_precondition}} |
| {{func_req_2_id}} | {{func_req_2_name}} | {{func_req_2_priority}} | {{func_req_2_desc}} | {{func_req_2_input}} | {{func_req_2_output}} | {{func_req_2_precondition}} |

## 五、非功能需求

- **性能**: 响应时间不超过 {{perf_response_time}}，支持 {{perf_concurrent_users}} 并发
- **可用性**: 系统可用率不低于 {{perf_availability}}
- **安全性**: {{security_requirement}}
- **可维护性**: {{maintainability_requirement}}
- **可扩展性**: {{scalability_requirement}}

## 六、接口设计

| 接口编号 | 接口名称 | 对端系统 | 协议 | 数据格式 | 说明 |
| -------- | -------- | -------- | ---- | -------- | ---- |
| {{if_1_id}} | {{if_1_name}} | {{if_1_system}} | {{if_1_protocol}} | {{if_1_format}} | {{if_1_desc}} |
| {{if_2_id}} | {{if_2_name}} | {{if_2_system}} | {{if_2_protocol}} | {{if_2_format}} | {{if_2_desc}} |

## 七、数据字典

| 数据项 | 类型 | 长度 | 必填 | 默认值 | 说明 |
| ------ | ---- | ---- | ---- | ------ | ---- |
| {{dd_1_name}} | {{dd_1_type}} | {{dd_1_length}} | {{dd_1_required}} | {{dd_1_default}} | {{dd_1_desc}} |
| {{dd_2_name}} | {{dd_2_type}} | {{dd_2_length}} | {{dd_2_required}} | {{dd_2_default}} | {{dd_2_desc}} |

## 八、约束条件

{{#each constraints}}
- {{this}}
{{/each}}

## 九、附录

{{appendix_content}}

---

> 本文档由 {{author}} 于 {{create_date}} 编制。
