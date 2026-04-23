# 合规状态报告

| 字段     | 内容                       |
| -------- | -------------------------- |
| 项目名称 | {{project_name}}           |
| 编制人   | {{author}}                 |
| 编制日期 | {{create_date}}            |
| 文档版本 | {{document_version}}       |

| 报告周期 | {{report_period_start}} ~ {{report_period_end}} |
| -------- | ------------------------------------------------ |
| 密级     | {{classification_level}}                         |
| 监管要求 | {{regulatory_framework}}                         |

---

## 一、合规检查清单

| 检查编号 | 检查项目         | 合规标准     | 检查结果 | 整改状态 | 责任人       | 截止日期     |
| -------- | ---------------- | ------------ | -------- | -------- | ------------ | ------------ |
| {{chk_1_id}} | {{chk_1_item}} | {{chk_1_standard}} | {{chk_1_result}} | {{chk_1_rectify}} | {{chk_1_owner}} | {{chk_1_due}} |
| {{chk_2_id}} | {{chk_2_item}} | {{chk_2_standard}} | {{chk_2_result}} | {{chk_2_rectify}} | {{chk_2_owner}} | {{chk_2_due}} |
| {{chk_3_id}} | {{chk_3_item}} | {{chk_3_standard}} | {{chk_3_result}} | {{chk_3_rectify}} | {{chk_3_owner}} | {{chk_3_due}} |

- **合规达标率**: {{compliance_rate}}%
- **待整改项数**: {{pending_rectification_count}}

## 二、安全审计状态

- **审计周期**: {{audit_period}} | **审计范围**: {{audit_scope}} | **审计机构**: {{audit_org}}

| 发现编号 | 问题描述         | 风险等级 | 整改措施       | 整改状态 | 验证日期     |
| -------- | ---------------- | -------- | -------------- | -------- | ------------ |
| {{find_1_id}} | {{find_1_desc}} | {{find_1_risk}} | {{find_1_action}} | {{find_1_status}} | {{find_1_verify}} |
| {{find_2_id}} | {{find_2_desc}} | {{find_2_risk}} | {{find_2_action}} | {{find_2_status}} | {{find_2_verify}} |

## 三、等级保护进展

- **等保等级**: {{mlps_level}} | **测评机构**: {{mlps_evaluator}} | **当前阶段**: {{mlps_phase}}

| 控制域       | 要求项数 | 已达标   | 未达标   | 达标率     |
| ------------ | -------- | -------- | -------- | ---------- |
| 安全物理环境 | {{phy_total}} | {{phy_pass}} | {{phy_fail}} | {{phy_rate}}% |
| 安全通信网络 | {{net_total}} | {{net_pass}} | {{net_fail}} | {{net_rate}}% |
| 安全区域边界 | {{border_total}} | {{border_pass}} | {{border_fail}} | {{border_rate}}% |
| 安全计算环境 | {{compute_total}} | {{compute_pass}} | {{compute_fail}} | {{compute_rate}}% |
| 安全管理中心 | {{mgmt_total}} | {{mgmt_pass}} | {{mgmt_fail}} | {{mgmt_rate}}% |

## 四、数据安全检查

| 检查项目     | 标准要求         | 实际状态 | 合规     | 备注         |
| ------------ | ---------------- | -------- | -------- | ------------ |
| 数据分类分级 | {{ds_1_std}}     | {{ds_1_actual}} | {{ds_1_compliant}} | {{ds_1_note}} |
| 数据加密传输 | {{ds_2_std}}     | {{ds_2_actual}} | {{ds_2_compliant}} | {{ds_2_note}} |
| 数据加密存储 | {{ds_3_std}}     | {{ds_3_actual}} | {{ds_3_compliant}} | {{ds_3_note}} |
| 数据脱敏     | {{ds_4_std}}     | {{ds_4_actual}} | {{ds_4_compliant}} | {{ds_4_note}} |
| 数据备份恢复 | {{ds_5_std}}     | {{ds_5_actual}} | {{ds_5_compliant}} | {{ds_5_note}} |

## 五、访问控制审计

| 审计项目     | 检查内容         | 检查结果 | 异常数   | 处理状态     |
| ------------ | ---------------- | -------- | -------- | ------------ |
| 账号权限审查 | {{ac_1_content}} | {{ac_1_result}} | {{ac_1_anomaly}} | {{ac_1_status}} |
| 特权操作审计 | {{ac_2_content}} | {{ac_2_result}} | {{ac_2_anomaly}} | {{ac_2_status}} |
| 登录行为分析 | {{ac_3_content}} | {{ac_3_result}} | {{ac_3_anomaly}} | {{ac_3_status}} |
| API调用审计  | {{ac_4_content}} | {{ac_4_result}} | {{ac_4_anomaly}} | {{ac_4_status}} |

## 六、整改事项跟踪

| 整改编号 | 来源         | 问题描述         | 整改措施       | 责任人       | 截止日期     | 当前状态 |
| -------- | ------------ | ---------------- | -------------- | ------------ | ------------ | -------- |
| {{rect_1_id}} | {{rect_1_source}} | {{rect_1_desc}} | {{rect_1_action}} | {{rect_1_owner}} | {{rect_1_due}} | {{rect_1_status}} |
| {{rect_2_id}} | {{rect_2_source}} | {{rect_2_desc}} | {{rect_2_action}} | {{rect_2_owner}} | {{rect_2_due}} | {{rect_2_status}} |

- **整改完成率**: {{rectification_rate}}%
- **逾期未整改项**: {{overdue_count}}

---

> 本报告由 {{author}} 于 {{create_date}} 编制。本文档涉及金融合规敏感信息，请按密级要求妥善保管与传递。
