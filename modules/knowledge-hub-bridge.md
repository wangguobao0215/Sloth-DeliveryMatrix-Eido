# Sloth-DeliveryMatrix-Eido Knowledge Hub Bridge

> 交付矩阵指挥官 × 中央知识库集成协议（v2.0.0 — 双树架构）
> 仅当 EXTEND.md 中 `knowledge_hub.enabled = true` 时生效。

---

## 知识结晶点（Skill → Hub）

当以下操作完成后，AI **应当**向用户展示预填好的萃取建议卡片，经用户确认后写入中央库。

> v1.0 阶段仅激活 `priority: high` 的结晶点。`medium`/`low` 级别为 opt-in，用户可在 EXTEND.md 中配置。

| 触发条件 | 产出 asset_type | 目标节点 | priority | 萃取要素 |
|---------|----------------|---------|----------|---------|
| 完成项目复盘（项目结项/里程碑复盘） | `lesson_learned` | C4 + S*（视项目域） | **high** | 项目概况、关键事件、经验教训、改进建议 |
| 风险处理成功记录（Risk Radar） | `risk_pattern` | C4 + S*（视项目域） | **high** | 风险描述、发现时机、处理方案、效果评估 |
| 交付最佳实践沉淀 | `best_practice` | C4 | medium | 做法描述、适用场景、效果数据、实施前提 |
| 验收通过的交付方法论 | `methodology` | C4 | medium | 方法论框架、适用项目类型、关键步骤、质量标准 |

### 萃取规则

> 工作流：AI 检测到结晶点 → 预填萃取卡片（含 title/summary/confidence） → 用户确认或微调 → 提交注册。用户可选择「跳过本次」但系统会在下次相同场景再次提示。

1. **项目复盘 → lesson_learned**：
   - `title`："{客户名} {项目名} 交付复盘"
   - `summary`：核心经验教训和关键改进建议
   - `industry`：从项目信息提取
   - `customer_type`：从客户画像提取
   - `capability_node`：`C4`
   - `scenario_nodes`：从项目业务域提取，如 `["S4"]`（制造项目）、`["S5"]`（质量项目）、`["S4", "S5"]`（制造+质量综合项目）
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `confidence`：A（有完整项目数据 + 客户反馈）; B（仅内部复盘）
   - `content`：项目背景 → 范围与目标 → 关键里程碑 → 遇到的问题 → 根因分析 → 改进措施 → 可复用经验
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-MfgConsult-Eido, Sloth-StratAlign-Eido]`

2. **风险处理 → risk_pattern**：
   - `title`："{项目类型} 风险模式：{风险简述}"
   - `summary`：风险早期信号和有效应对方案
   - `capability_node`：`C4`
   - `scenario_nodes`：从项目业务域提取，如 `["S4.2"]`（MES 项目风险）、`["S3.1"]`（供应链项目风险）
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `confidence`：B（单次处理）; A（出现 2+ 次同类风险并有效处理）
   - `content`：风险描述 → 早期信号 → 触发条件 → 影响评估 → 应对方案 → 经验总结
   - `tags`：`[delivery-risk, {风险类别}]`
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-MfgConsult-Eido]`

3. **最佳实践 → best_practice**（medium）：
   - `title`："{场景} 交付最佳实践"
   - `summary`：做法核心要点和适用前提
   - `capability_node`：`C4`
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `tags`：`[delivery, implementation]`

4. **交付方法论 → methodology**（medium）：
   - `title`："{项目类型} 交付方法论"
   - `summary`：方法论核心步骤和质量标准
   - `capability_node`：`C4`
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `tags`：`[delivery-methodology, {项目类型}]`

---

## 知识需求点（Hub → Skill）

当用户启动以下操作时，AI **应当**先查询中央库获取相关知识推荐。

| 触发条件 | 查询维度 | 上下文信号 |
|---------|---------|----------|
| 启动新项目（项目初始化） | `scenario_node` 匹配项目业务域（如 `S4`/`S5`）获取同域教训 + `capability_node=C4` 获取交付方法和风险模式 | 项目类型、客户行业、项目规模 |
| 启动风险评估（Risk Radar） | `scenario_node` 匹配项目域获取同域风险模式 + `capability_node=C4` 获取通用交付风险 | 项目类型、当前阶段 |
| 启动里程碑评审 | `capability_node=C4` 获取交付最佳实践和方法论 | 当前里程碑类型 |
| 启动验收交付 | `scenario_node` 匹配项目域获取成功案例 + `capability_node=C5` 获取客户成功 Playbook | 客户行业、项目类型 |

### 推荐展示规则

> 有匹配结果时展示推荐卡片（最多 3 条），用户可选择查看详情或直接继续。无匹配则静默跳过。

1. **新项目启动**：通过 `scenario_node` 前缀匹配推荐同域项目的经验教训和已识别风险模式，这是交付最核心的知识需求。
2. **风险评估**：通过 `scenario_node` 推荐同域历史风险模式，结合 `capability_node=C4` 补充通用交付风险，帮助预判可能遇到的坑。
3. **里程碑评审**：通过 `capability_node=C4` 推荐交付最佳实践和方法论，作为评审标准的参考。
4. **验收交付**：通过 `scenario_node` 推荐同域成功交付案例，结合 `capability_node=C5` 获取客户成功 Playbook，为验收会议提供信心。

---

## 反馈通道

当用户在本 Skill 中引用了 Hub 推荐的知识资产后，AI 应当在任务完成时询问："这条知识对你有帮助吗？（有用 / 过时 / 有误）"，并通过 `record_feedback.py` 记录反馈，驱动知识质量自动演化。
