"""转导师工单表：学生提出、知识库无法直接作答或需导师介入的问题。

对应任务书"无依据拒答并转导师工单"；03 阶段先作为数据库增删改查的预演表，
04 问答闭环直接复用。
"""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from packages.common.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    question: Mapped[str] = mapped_column(Text, nullable=False, comment="学生问题")
    answer: Mapped[str | None] = mapped_column(Text, nullable=True, comment="导师作答，未答为空")
    # pending 待作答 / answered 已作答 / closed 已关闭
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    # concept 概念答疑 / homework 作业求解（教学护栏分流标记）
    scene: Mapped[str | None] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
