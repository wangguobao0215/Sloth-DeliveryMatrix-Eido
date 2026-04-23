# 会议纪要

| 字段     | 内容                   |
| -------- | ---------------------- |
| 会议主题 | {{meeting_subject}}    |
| 日期时间 | {{meeting_datetime}}   |
| 会议地点 | {{meeting_location}}   |
| 参会人员 | {{attendees}}          |
| 记录人   | {{recorder}}           |

---

## 一、议程回顾

{{#each agenda_items}}
{{@index}}. {{this}}
{{/each}}

## 二、讨论要点

{{#each discussion_points}}
### 议题 {{@index}}: {{this.topic}}

- **背景**: {{this.background}}
- **讨论内容**: {{this.content}}
- **结论**: {{this.conclusion}}
{{/each}}

## 三、决策记录

| 编号 | 决策内容         | 提议人       | 决策结果   | 备注         |
| ---- | ---------------- | ------------ | ---------- | ------------ |
| {{decision_1_id}} | {{decision_1_content}} | {{decision_1_proposer}} | {{decision_1_result}} | {{decision_1_note}} |

## 四、行动项

| 编号 | 行动项描述       | 责任人       | 截止日期     | 当前状态 |
| ---- | ---------------- | ------------ | ------------ | -------- |
| {{action_1_id}} | {{action_1_desc}} | {{action_1_owner}} | {{action_1_deadline}} | {{action_1_status}} |
| {{action_2_id}} | {{action_2_desc}} | {{action_2_owner}} | {{action_2_deadline}} | {{action_2_status}} |

## 五、下次会议安排

- **预定时间**: {{next_meeting_datetime}}
- **预定地点**: {{next_meeting_location}}
- **预定议题**: {{next_meeting_agenda}}

---

> 记录人: {{recorder}} | 日期: {{meeting_date}}
