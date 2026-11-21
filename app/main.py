"""FastAPI 应用入口（AI_EDU RAG 知识库问答模块）。

启动（项目根目录下）：
    venv\Scripts\python -m uvicorn app.main:app --reload
自动文档：http://127.0.0.1:8000/docs
"""
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from packages.common.database import get_db
from packages.rag import api
from app.routers import practice

app = FastAPI(title="AI_EDU RAG 知识库问答模块")

app.include_router(api.router)
app.include_router(practice.router)


@app.get("/health", tags=["system"])
def health(db: Session = Depends(get_db)):
    """健康检查：能连上数据库即返回 ok。"""
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
