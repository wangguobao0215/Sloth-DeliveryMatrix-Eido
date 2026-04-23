# 项目交接文档

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

---

## 一、项目基本信息

| 字段         | 内容                               |
| ------------ | ---------------------------------- |
| 项目编号     | {{project_id}}                     |
| 甲方/乙方   | {{client_org}} / {{vendor_org}}    |
| 项目经理     | {{pm_name}}                        |
| 项目起止日期 | {{project_start}} ~ {{project_end}} |
| 移交方/接收方| {{from_party}} / {{to_party}}      |
| 交接日期     | {{handover_date}}                  |

## 二、交接范围

{{#each handover_scope_items}}
- {{this}}
{{/each}}

## 三、系统架构概览

- **前端**: {{frontend_stack}} | **后端**: {{backend_stack}} | **数据库**: {{database_stack}}
- **部署方式**: {{deployment_mode}}
- **架构说明**: {{system_topology_desc}}

| 服务名称 | 部署地址 | 端口 | 说明 |
| -------- | -------- | ---- | ---- |
| {{svc_1_name}} | {{svc_1_addr}} | {{svc_1_port}} | {{svc_1_desc}} |
| {{svc_2_name}} | {{svc_2_addr}} | {{svc_2_port}} | {{svc_2_desc}} |

## 四、账号与权限清单

| 系统/平台 | 账号 | 权限级别 | 持有人 | 备注 |
| --------- | ---- | -------- | ------ | ---- |
| {{acct_1_system}} | {{acct_1_account}} | {{acct_1_level}} | {{acct_1_owner}} | {{acct_1_note}} |
| {{acct_2_system}} | {{acct_2_account}} | {{acct_2_level}} | {{acct_2_owner}} | {{acct_2_note}} |

> **注意**: 敏感密码信息请通过加密渠道单独传递，不记录在本文档中。

## 五、运维手册摘要

- **日常运维**: {{daily_ops_summary}}
- **备份策略**: {{backup_frequency}}，存储于 {{backup_storage}}
- **监控告警**: {{monitoring_tool}}，告警渠道 {{alert_channel}}

## 六、已知问题与待办事项

| 类型 | 编号 | 描述 | 严重程度/优先级 | 负责人 | 备注 |
| ---- | ---- | ---- | -------------- | ------ | ---- |
| 问题 | {{issue_1_id}} | {{issue_1_desc}} | {{issue_1_severity}} | {{issue_1_owner}} | {{issue_1_note}} |
| 待办 | {{todo_1_id}} | {{todo_1_desc}} | {{todo_1_priority}} | {{todo_1_owner}} | {{todo_1_due}} |

## 七、紧急联系人

| 角色 | 姓名 | 电话 | 邮箱 | 职责 |
| ---- | ---- | ---- | ---- | ---- |
| {{contact_1_role}} | {{contact_1_name}} | {{contact_1_phone}} | {{contact_1_email}} | {{contact_1_duty}} |
| {{contact_2_role}} | {{contact_2_name}} | {{contact_2_phone}} | {{contact_2_email}} | {{contact_2_duty}} |

## 八、交接确认签字区

| 角色   | 姓名            | 签字 | 日期                   |
| ------ | --------------- | ---- | ---------------------- |
| 移交方 | {{from_signer}} |      | {{from_sign_date}}     |
| 接收方 | {{to_signer}}   |      | {{to_sign_date}}       |
| 见证人 | {{witness}}     |      | {{witness_sign_date}}  |

---

> 本文档由 {{author}} 于 {{create_date}} 编制。交接双方确认签字后生效。
