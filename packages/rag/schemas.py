"""工单接口的请求体 / 响应体模型。"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TicketCreate(BaseModel):
    """学生提交问题、生成工单。"""

    question: str = Field(..., min_length=1, description="学生问题")
    scene: str | None = Field(default=None, description="concept 概念答疑 / homework 作业求解")


class TicketAnswer(BaseModel):
    """导师作答请求体。"""

    answer: str = Field(..., min_length=1, description="导师给出的回答")


class TicketOut(BaseModel):
    """工单响应体。"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    answer: str | None
    status: str
    scene: str | None
    created_at: datetime
