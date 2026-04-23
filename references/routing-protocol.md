# 路由协议 (Routing Protocol)

> DeliveryMatrix 意图识别与技能路由的核心协议。所有用户输入必须经过本协议匹配后再分派到目标技能。

---

## 一、三层匹配机制

路由按优先级从高到低依次尝试三层匹配，命中即停：

### Layer-1: 关键词精确匹配
- 直接命中预定义触发词，零延迟路由。
- 示例：用户输入含「周报」→ 命中 `weekly_report` 路由。

### Layer-2: 正则模式匹配
- 对 Layer-1 未命中的输入，执行正则表达式扫描。
- 支持中文分词后的组合匹配，如 `(风险|问题).*(升级|上报)` → 命中 `escalation` 路由。
- 正则库按业务域分组维护，避免全量扫描。

### Layer-3: LLM 语义匹配
- 前两层均未命中时，将用户输入 + 当前项目上下文送入 LLM 做意图分类。
- LLM 返回 `{intent, confidence, matched_route_id}`。
- confidence < 0.6 时进入 fallback 流程。

---

## 二、路由表 Schema

```yaml
route:
  id: string            # 唯一标识，如 "rt_weekly_report"
  name: string          # 路由名称，如 "生成周报"
  target_skill: string  # 目标技能 ID，如 "report_generator"
  triggers:
    keywords: list[str]       # Layer-1 关键词列表
    regex_patterns: list[str] # Layer-2 正则列表
    semantic_hints: list[str] # Layer-3 语义提示（供 LLM 参考）
  context_injection:
    required: list[str]   # 必须注入的上下文字段，如 ["project_id", "sprint_id"]
    optional: list[str]   # 可选上下文字段
  parameters:
    required: list[str]   # 必需参数
    optional: list[str]   # 可选参数
    defaults: dict        # 参数默认值
  priority: int           # 路由优先级，数字越小优先级越高
  enabled: bool           # 是否启用
```

---

## 三、复合路由编排模式

当一个用户意图需要多个技能协作时，使用复合路由：

### parallel_then_merge（并行后合并）
- 同时调用多个技能，汇总结果后统一输出。
- 适用场景：「给我一份项目全景报告」→ 并行调用进度统计、风险汇总、资源概览，合并为一份报告。

### sequential（顺序执行）
- 技能按依赖顺序执行，前一技能的输出作为后一技能的输入。
- 适用场景：「分析本周延期任务并生成整改计划」→ 先调用延期分析，再调用计划生成。

### conditional（条件分支）
- 根据运行时条件选择不同路由路径。
- 适用场景：「检查项目健康度」→ 如果 SPI < 0.85 则触发预警路由，否则走常规汇报路由。

---

## 四、Fallback 策略

### no_match（无匹配）
- 三层匹配均未命中。
- 处理：向用户确认意图，提供 Top-3 候选路由供选择。
- 输出格式：「我理解您可能想要：1) ... 2) ... 3) ... 请选择或重新描述。」

### ambiguous_match（模糊匹配）
- 多条路由 confidence 差距 < 0.15，无法明确判定。
- 处理：列出候选路由并附带简要说明，让用户确认。

### skill_unavailable（技能不可用）
- 目标技能加载失败或超时。
- 处理：记录错误日志，尝试降级方案（如用通用模板替代专用技能），通知用户当前能力受限。

---

## 五、路由决策示例

| 用户输入 | Layer | 命中路由 | 说明 |
|---------|-------|---------|------|
| 「生成本周周报」 | L1-关键词 | rt_weekly_report | 精确匹配「周报」 |
| 「看下近三个迭代的燃尽图趋势」 | L2-正则 | rt_burndown_analysis | 匹配 `燃尽图.*趋势` |
| 「最近团队氛围不太好，怎么处理」 | L3-语义 | rt_team_health | LLM 识别为团队健康度问题 |
| 「这个需求能不能做」 | L3-语义 | rt_feasibility_check | LLM 结合项目上下文判断为可行性评估 |
| 「帮我订个会议室」 | Fallback | no_match | 超出 DeliveryMatrix 能力范围 |
