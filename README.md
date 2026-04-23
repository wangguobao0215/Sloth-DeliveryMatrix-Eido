<p align="center">
  <img src="assets/sloth-avatar-round.png" width="120" />
</p>

<h1 align="center">Sloth-DeliveryMatrix-Eido</h1>

<p align="center">
  <strong>深达 · 交付管理 — 软件项目团队的 AI 原生交付智能体</strong><br/>
  三角色编排 + 九大原子能力，覆盖交付全流程
</p>

<p align="center">
  <img src="assets/qrcode.jpg" width="140" /><br/>
  <sub>扫码关注 <strong>树懒老K</strong> · 获取更多 AI 技能</sub><br/>
  <em>慢一点，深一度</em>
</p>

[![QoderWork Skill](https://img.shields.io/badge/QoderWork-Skill-blue)](https://docs.qoder.com/qoderwork/introduction)
[![Version](https://img.shields.io/badge/version-1.0.0-green)]()
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

[English](README_EN.md) | 中文

---

## 品名释义

> **深达**——「深」取自树懒老K品牌哲学「慢一点，深一度」，「达」意为达成、送达。项目交付的终极目标是深度达成客户期望，而非仅仅完成里程碑。深达，深度达成每一个交付承诺。

## 功能概览

- **三角色编排**：PM 指挥官 / 交付总监 / 技术顾问，一套技能包覆盖交付全团队
- **九大原子能力**：文档生成、会议纪要、风险雷达、进度追踪、资源协调、客户沟通、需求分析、验收交付、数据采集
- **结构化路由**：双层路由引擎（关键词 + 正则 + 语义），精准匹配用户意图
- **状态外置**：项目状态持久化为 YAML 文件，跨会话、跨角色共享
- **本土适配**：云之家/飞书/钉钉数据采集，GB/T 政企文档规范，中国交付实践
- **多 Skill 编排**：并行合并、顺序执行、条件分支三种编排模式

## 适用场景

- **项目经理**：周报/日报生成、会议纪要、风险评估、进度追踪
- **交付总监**：跨项目全景仪表盘、资源调度、项目健康度排名
- **技术顾问**：需求分析、方案论证、GAP 分析、技术风险评估

## 快速开始

1. 在 QoderWork 中安装本技能
2. 首次使用时输入"帮我写周报"，系统将引导你创建第一个项目
3. 项目创建后，可直接使用所有能力

常用命令示例：
- "帮我写本周周报"
- "整理一下今天的会议纪要"
- "评估一下项目风险"
- "项目进度怎么样了"
- "给客户写个状态更新邮件"
- "准备明天的项目评审材料"（复合编排）

## 文档

- [详细用户手册](references/user-guide.md) -- 完整使用指南、最佳实践与常见问题

## 目录结构

```
Sloth-DeliveryMatrix-Eido/
├── SKILL.md              # 主指令文件（Agent 入口）
├── README.md             # 本文件（中文）
├── README_EN.md          # 英文说明
├── LICENSE               # MIT 许可证
├── CHANGELOG.md          # 版本变更日志
├── modules/              # 九大原子能力模块
├── references/           # 知识库与协议文档
├── templates/            # 文档模板（基础模板 + GB/T 政企模板）
├── scripts/              # Python 辅助脚本
└── schemas/              # 数据 Schema 定义
```

## 版本

当前版本：1.0.0

## 许可证

MIT License
