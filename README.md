# AI_EDU 教学智能体 · RAG 知识库问答模块

面向《Python 程序设计》《数据结构与算法》《计算机网络》等课程的 RAG 问答模块：学生提问 → 检索课程知识库 → 有依据作答，无依据拒答并转导师工单，导师作答后可一键回灌知识库。

本项目为本科毕业设计，模块化组织在 `packages/` 下，便于后续并入 AI_EDU 主仓。

## 目录结构

```
ai-edu-rag/
├── app/                  # 服务入口与练习路由
│   ├── main.py           # FastAPI 入口，挂载 /health 与各模块路由
│   └── routers/          # 阶段练习（第 1 周内存版）
├── packages/
│   ├── common/           # 配置读取、数据库引擎与会话
│   ├── llm/              # 统一大模型调用层（OpenAI 兼容）
│   ├── rag/              # 工单模型、请求响应体、接口路由
│   ├── tools/            # 落地性检查：标出低支撑句子
│   └── agents/           # 追问引擎、教学流程
├── scripts/init_db.py    # 初始化 pgvector 扩展与数据表
├── tests/                # 冒烟测试
└── data/                 # 本地课程语料（不入库）
```

## 功能进度

- [x] FastAPI 工程底座、配置分层、健康检查
- [x] 转导师工单表与接口骨架
- [ ] 文档入库（PDF / Word / Markdown）
- [ ] 混合检索（BM25 + 向量 + RRF + 重排）
- [ ] 无依据拒答与工单闭环
- [ ] 导师作答回灌知识库
- [ ] 轻量课程知识图谱
- [ ] 评测集与 RAGAS 评测

## 本地运行

要求 Python 3.11、PostgreSQL 16 + pgvector。

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env      # 填入自己的 API Key 与数据库密码
venv\Scripts\python scripts\init_db.py
venv\Scripts\python -m uvicorn app.main:app --reload
```

打开 http://127.0.0.1:8000/docs 查看接口文档。

## 说明

- 仓库内不含任何真实密钥、数据库密码与课程原始语料。
- 本地模型（bge-m3、bge-reranker）体积较大，不纳入版本管理。
