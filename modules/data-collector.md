# Data Collector - 数据采集能力模块

> 模块类型: 能力模块 (Capability Module)
> 调用方式: 系统初始化时自动加载，或用户说"导入数据""同步数据""连接XX平台"时触发

## 1. 模块职责

本模块负责从多种协作平台和数据源中采集项目交付相关数据，进行智能标注和归一化处理，转化为统一的项目状态数据格式，供其他模块使用。

## 2. 多平台适配器架构

### 2.1 平台支持矩阵

| 平台 | 优先级 | 数据类型 | 接入方式 | 状态 |
|------|--------|---------|---------|------|
| 云之家 (Yunzhijia) | 主要 | 消息、任务、审批、日程 | API + Webhook | 首选 |
| 飞书 (Feishu/Lark) | 次要 | 消息、任务、审批、日程、文档 | API | 支持 |
| 钉钉 (DingTalk) | 次要 | 消息、任务、审批、日程 | API | 支持 |
| 企业微信 (WeCom) | 次要 | 消息、任务、审批、日程 | API | 支持 |
| 邮件 (Email) | 补充 | 邮件内容、附件 | IMAP/用户转发 | 支持 |
| Excel/CSV | 降级 | 结构化数据 | 文件导入 | 支持 |
| 用户手动粘贴 | 兜底 | 任意文本 | 对话输入 | 始终可用 |

### 2.2 适配器接口规范

每个平台适配器必须实现以下统一接口：

```
接口定义:

adapter.get_messages(project_id, date_range)
  → 返回: [{sender, content, timestamp, channel, attachments}]

adapter.get_tasks(project_id)
  → 返回: [{task_id, title, assignee, status, due_date, priority, tags}]

adapter.get_approvals(project_id, date_range)
  → 返回: [{approval_id, type, title, initiator, status, approvers, result}]

adapter.get_calendar(project_id, date_range)
  → 返回: [{event_id, title, time_start, time_end, attendees, location}]

adapter.get_documents(project_id)
  → 返回: [{doc_id, title, last_modified, author, url}]
```

### 2.3 平台切换逻辑

```
数据采集优先级:
1. 检查 project.platform 配置
2. 尝试通过 API 连接指定平台
3. 如果 API 不可用:
   a. 提示用户检查 API 配置
   b. 建议降级方案（手动粘贴或 Excel 导入）
4. 如果用户使用多个平台:
   a. 分别采集各平台数据
   b. 按时间线合并
   c. 去重（基于内容相似度和时间戳）
```

### 2.4 平台优先级

当多个数据源可用时，按以下优先级采集：

1. **项目管理工具**（Jira / 禅道 / Ones）— 进度和任务数据最权威
2. **代码仓库**（GitLab / GitHub）— 提交频率、MR数据客观可量化
3. **协作平台**（飞书/钉钉/企微/云之家）— 沟通记录、审批流
4. **文档平台**（Confluence / 语雀 / 飞书文档）— 文档更新记录
5. **手动输入** — 兜底方案，当自动采集不可用时

同一指标从多个平台采集到时，取项目管理工具的数据为准，其他来源作为交叉验证。

## 3. 统一数据接口

### 3.1 消息数据格式

```json
{
  "type": "message",
  "source_platform": "yunzhijia",
  "project_id": "SP-2024-001",
  "data": {
    "sender": "张三",
    "sender_role": "developer",
    "content": "接口联调完成，但发现性能问题，查询响应时间超过3秒",
    "timestamp": "2024-01-15T14:30:00+08:00",
    "channel": "智慧园区-开发群",
    "attachments": [],
    "tags": ["progress_update", "risk_signal"],
    "extracted_items": {
      "decisions": [],
      "action_items": [],
      "risk_signals": ["性能问题: 查询响应时间超过3秒"]
    }
  }
}
```

### 3.2 任务数据格式

```json
{
  "type": "task",
  "source_platform": "feishu",
  "project_id": "SP-2024-001",
  "data": {
    "task_id": "T-001",
    "title": "完成用户管理模块接口开发",
    "description": "...",
    "assignee": "李四",
    "status": "in_progress",
    "priority": "high",
    "created_date": "2024-01-10",
    "due_date": "2024-01-18",
    "actual_complete_date": null,
    "tags": ["backend", "user_module"],
    "subtasks": [],
    "comments": []
  }
}
```

### 3.3 审批数据格式

```json
{
  "type": "approval",
  "source_platform": "dingtalk",
  "project_id": "SP-2024-001",
  "data": {
    "approval_id": "APR-001",
    "approval_type": "change_request",
    "title": "需求变更: 新增报表导出功能",
    "initiator": "张三",
    "status": "approved",
    "approvers": [
      {"name": "PM王", "result": "approved", "comment": "同意"},
      {"name": "总监李", "result": "approved", "comment": "注意工期影响"}
    ],
    "submit_date": "2024-01-12",
    "complete_date": "2024-01-13"
  }
}
```

## 4. 智能标注引擎

### 4.1 LLM 标注任务

对采集到的非结构化数据（消息、评论等），使用 LLM 进行智能标注：

| 标注类型 | 描述 | 标注标签 |
|---------|------|---------|
| 决策标注 | 识别对话中的决策和结论 | `decision` |
| 行动项标注 | 识别任务分配和待办事项 | `action_item` |
| 风险信号标注 | 识别潜在风险和问题 | `risk_signal` |
| 进度更新标注 | 识别进度汇报信息 | `progress_update` |
| 情绪标注 | 识别负面情绪或不满 | `sentiment_negative` |
| 阻塞标注 | 识别阻塞性问题 | `blocker` |
| 需求变更标注 | 识别需求变更请求 | `change_request` |

### 4.2 标注处理流程

```
原始消息输入
    ↓
第一轮: 快速分类 (是否与项目交付相关)
  ├── 不相关: 跳过 (如日常闲聊、节日问候)
  └── 相关: 进入第二轮
    ↓
第二轮: 多标签标注 (一条消息可能有多个标签)
    ↓
第三轮: 关键信息提取
  ├── 决策: 提取决策内容、决策人
  ├── 行动项: 提取任务、责任人、时限
  ├── 风险: 提取风险描述、严重程度估计
  └── 进度: 提取完成情况、百分比
    ↓
输出: 标注后的结构化数据
```

### 4.3 标注质量控制

```
标注质量保障机制:
1. 置信度阈值: LLM标注置信度 < 70% 时，标记为"待人工确认"
2. 矛盾检测: 同一消息的标注互相矛盾时，保留所有标注并标记
3. 上下文关联: 结合前后消息进行标注（避免断章取义）
4. 定期校准: 用户反馈"标注错误"时，记录并优化标注策略
```

## 5. 降级策略

当 API 不可用或无法自动采集时，按以下顺序降级：

### 5.1 降级路径

```
Level 1: API 自动采集 (最佳)
  ↓ API不可用
Level 2: 用户粘贴聊天记录/邮件内容
  ↓ 用户无法提供文本
Level 3: Excel/CSV 导入 (结构化数据)
  ↓ 用户无文件
Level 4: 用户口述 (最基础)
  ↓ 完全无数据
Level 5: 基于历史模式估算 (标注为"估算")
```

### 5.2 用户粘贴处理

当用户粘贴聊天记录时的处理规则：

```
1. 自动识别格式:
   - 飞书格式: "[时间] 姓名: 内容"
   - 微信格式: "姓名 时间\n内容"
   - 钉钉格式: "姓名 (时间)\n内容"
   - 纯文本: 按段落切分

2. 解析为统一消息格式

3. 执行智能标注

4. 询问用户确认关键提取结果:
   "我从聊天记录中提取了以下信息，请确认是否准确:
    - 决策: [...]
    - 行动项: [...]
    - 风险: [...]"
```

### 5.3 Excel 导入规范

支持以下 Excel 格式导入：

```
任务数据导入格式:
| 任务名称 | 负责人 | 状态 | 开始日期 | 截止日期 | 优先级 | 备注 |

里程碑数据导入格式:
| 里程碑名称 | 计划开始 | 计划完成 | 实际完成 | 状态 |

团队数据导入格式:
| 姓名 | 角色 | 所属项目 | 分配比例 | 技能标签 |
```

## 6. 数据归一化

### 6.1 归一化到项目状态格式

所有采集的数据最终归一化为项目状态对象：

```json
{
  "project_id": "SP-2024-001",
  "project_name": "智慧园区一期",
  "last_updated": "2024-01-15T18:00:00+08:00",
  "data_sources": ["yunzhijia_api", "user_paste"],
  "data_freshness": "fresh",
  "milestones": [...],
  "current_phase": "development",
  "tasks": [...],
  "team": [...],
  "risks": [...],
  "decisions": [...],
  "action_items": [...],
  "recent_activities": [...]
}
```

### 6.2 数据新鲜度标注

| 标签 | 定义 | 对分析的影响 |
|------|------|------------|
| `fresh` | 数据更新于24小时内 | 分析结果可信 |
| `recent` | 数据更新于1-7天内 | 分析结果基本可信，标注时间 |
| `stale` | 数据更新于7-30天内 | 分析结果需谨慎使用，建议刷新 |
| `outdated` | 数据更新超过30天 | 分析结果仅供参考，强烈建议刷新 |

每次输出分析结果时，必须在头部标注数据新鲜度。
