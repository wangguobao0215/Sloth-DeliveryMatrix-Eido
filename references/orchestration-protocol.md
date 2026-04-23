# 多技能编排协议 (Orchestration Protocol)

> 定义 DeliveryMatrix 在调用多个子技能时的输入输出规范、编排模式和错误处理机制。

---

## 一、标准输入格式 (skill_input)

所有技能调用统一使用以下输入结构：

```yaml
skill_input:
  intent: string              # 用户意图标识，如 "generate_weekly_report"
  parameters:                 # 业务参数
    sprint_id: "sprint_42"
    date_range: ["2026-04-14", "2026-04-20"]
    format: "markdown"
  project_context:            # 项目上下文（由状态协议注入）
    project_id: "proj_abc"
    project_name: "智慧园区二期"
    current_sprint: "sprint_42"
    team_size: 12
  upstream_data: object|null  # 上游技能的输出（sequential 模式下传递）
  execution_metadata:
    request_id: string        # 本次调用的唯一请求 ID
    caller: string            # 调用方标识
    timeout_ms: int           # 超时时间，默认 30000
    retry_policy: string      # 重试策略：none | once | exponential
```

---

## 二、标准输出格式 (skill_output)

所有技能必须返回以下结构：

```yaml
skill_output:
  status: "success" | "partial" | "error"
  primary_output: string        # 面向用户的主要输出内容（Markdown 格式）
  structured_data: object|null  # 机器可读的结构化数据，供下游技能消费
  side_effects:                 # 副作用列表（如状态写入、文件生成）
    - type: "state_update"
      target: "projects/proj_abc/risks.yaml"
      summary: "新增 1 条技术风险"
    - type: "file_created"
      path: "/outputs/weekly_report_0420.md"
  suggestions:                  # 后续建议操作
    - action: "review_risks"
      label: "查看完整风险清单"
    - action: "notify_stakeholders"
      label: "通知干系人"
  error_detail: object|null     # status 非 success 时填写
```

---

## 三、并行合并策略 (parallel_then_merge)

多个技能并行执行后，合并结果的规则：

1. **全部成功**：按预定义顺序拼接 `primary_output`，合并 `structured_data` 到统一对象。
2. **部分成功**：输出已成功部分的结果，对失败部分标注「该模块数据暂不可用」，不阻塞整体输出。
3. **全部失败**：汇总各技能错误信息，返回统一错误报告。

合并时 `side_effects` 和 `suggestions` 做去重后拼接。

---

## 四、顺序依赖处理 (sequential)

技能按声明顺序执行，遵循以下规则：

1. 前一技能的 `structured_data` 自动注入为下一技能的 `upstream_data`。
2. 前一技能 `status = "error"` 时，默认中断链路，返回已完成部分 + 错误位置。
3. 前一技能 `status = "partial"` 时，由编排器决定是否继续（配置项 `continue_on_partial: bool`）。
4. 每个技能独立计算超时，不共享全局超时。

---

## 五、错误传播规则

```
技能 A (error) ──→ 编排器捕获 ──→ 判断策略
                                      │
                    ┌─────────────────┼──────────────┐
                    ▼                 ▼              ▼
               abort_chain      skip_and_continue   retry
               (中断并报告)      (跳过继续执行)     (重试后再决策)
```

- **abort_chain**：默认策略，适用于强依赖场景。
- **skip_and_continue**：适用于可降级场景，跳过失败技能并在输出中标注。
- **retry**：按 `retry_policy` 重试，重试耗尽后降级为 abort 或 skip。

错误信息始终保留完整调用链路，便于排查：
```
[request_id=req_123] skillA(success) → skillB(error: timeout after 30s) → skillC(skipped)
```
