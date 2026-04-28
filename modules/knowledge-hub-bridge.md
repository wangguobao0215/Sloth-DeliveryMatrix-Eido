# Sloth-DeliveryMatrix-Eido Knowledge Hub Bridge

> 交付矩阵指挥官 × 中央知识库集成协议（v1.1.0）
> 仅当 EXTEND.md 中 `knowledge_hub.enabled = true` 时生效。

---

## 知识结晶点（Skill → Hub）

当以下操作完成后，AI **应当**向用户展示预填好的萃取建议卡片，经用户确认后写入中央库。

> v1.0 阶段仅激活 `priority: high` 的结晶点。`medium`/`low` 级别为 opt-in，用户可在 EXTEND.md 中配置。

| 触发条件 | 产出 asset_type | 目标 stage | priority | 萃取要素 |
|---------|----------------|-----------|----------|---------|
| 完成项目复盘（项目结项/里程碑复盘） | `lesson_learned` | `delivery` | **high** | 项目概况、关键事件、经验教训、改进建议 |
| 风险处理成功记录（Risk Radar） | `risk_pattern` | `delivery` | **high** | 风险描述、发现时机、处理方案、效果评估 |
| 交付最佳实践沉淀 | `best_practice` | `delivery` | medium | 做法描述、适用场景、效果数据、实施前提 |
| 验收通过的交付方法论 | `methodology` | `delivery` | medium | 方法论框架、适用项目类型、关键步骤、质量标准 |

### 萃取规则

> 工作流：AI 检测到结晶点 → 预填萃取卡片（含 title/summary/confidence） → 用户确认或微调 → 提交注册。用户可选择「跳过本次」但系统会在下次相同场景再次提示。

1. **项目复盘 → lesson_learned**：
   - `title`："{客户名} {项目名} 交付复盘"
   - `summary`：核心经验教训和关键改进建议
   - `industry`：从项目信息提取
   - `customer_type`：从客户画像提取
   - `confidence`：A（有完整项目数据 + 客户反馈）; B（仅内部复盘）
   - `content`：项目背景 → 范围与目标 → 关键里程碑 → 遇到的问题 → 根因分析 → 改进措施 → 可复用经验
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-MfgConsult-Eido, Sloth-StratAlign-Eido]`

2. **风险处理 → risk_pattern**：
   - `title`："{项目类型} 风险模式：{风险简述}"
   - `summary`：风险早期信号和有效应对方案
   - `confidence`：B（单次处理）; A（出现 2+ 次同类风险并有效处理）
   - `content`：风险描述 → 早期信号 → 触发条件 → 影响评估 → 应对方案 → 经验总结
   - `tags`：`[delivery-risk, {风险类别}]`
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-MfgConsult-Eido]`

3. **最佳实践 → best_practice**（medium）：
   - `title`："{场景} 交付最佳实践"
   - `summary`：做法核心要点和适用前提
   - `tags`：`[delivery, implementation]`

4. **交付方法论 → methodology**（medium）：
   - `title`："{项目类型} 交付方法论"
   - `summary`：方法论核心步骤和质量标准
   - `tags`：`[delivery-methodology, {项目类型}]`

---

## 知识需求点（Hub → Skill）

当用户启动以下操作时，AI **应当**先查询中央库获取相关知识推荐。

| 触发条件 | 查询维度 | 上下文信号 |
|---------|---------|----------|
| 启动新项目（项目初始化） | lesson_learned (same type) + risk_pattern + best_practice | 项目类型、客户行业、项目规模 |
| 启动风险评估（Risk Radar） | risk_pattern (same industry/type) + lesson_learned | 项目类型、当前阶段 |
| 启动里程碑评审 | best_practice (delivery) + methodology | 当前里程碑类型 |
| 启动验收交付 | case_study (successful delivery) + playbook | 客户行业、项目类型 |

### 推荐展示规则

> 有匹配结果时展示推荐卡片（最多 3 条），用户可选择查看详情或直接继续。无匹配则静默跳过。

1. **新项目启动**：优先推荐同类型项目的经验教训和已识别风险模式，这是交付最核心的知识需求。
2. **风险评估**：推荐同行业/同类型的历史风险模式，帮助预判可能遇到的坑。
3. **里程碑评审**：推荐交付最佳实践和方法论，作为评审标准的参考。
4. **验收交付**：推荐成功交付案例和客户成功 Playbook，为验收会议提供信心。

---

## 反馈通道

当用户在本 Skill 中引用了 Hub 推荐的知识资产后，AI 应当在任务完成时询问："这条知识对你有帮助吗？（有用 / 过时 / 有误）"，并通过 `record_feedback.py` 记录反馈，驱动知识质量自动演化。
