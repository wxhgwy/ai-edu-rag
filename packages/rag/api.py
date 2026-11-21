"""工单路由骨架。

业务增删改查由 03 模块第 2 周按每日任务自己实现；这里只留端点占位与 TODO，
保证服务能启动、自动文档能看到接口形状。
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from packages.common.database import get_db
from packages.rag.schemas import TicketAnswer, TicketOut

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    """工单队列（导师端查看未答/已答问题）。"""
    # TODO(03 第2周): 查询 Ticket，按 created_at 倒序返回；可加 status 过滤
    return []


@router.post("/{ticket_id}/answer", response_model=TicketOut)
def answer_ticket(ticket_id: int, payload: TicketAnswer, db: Session = Depends(get_db)):
    """导师作答：取工单 -> 写 answer -> status 置 answered。"""
    # TODO(03 第2周): 按 ticket_id 查 Ticket，查不到抛 404；
    #   写入 payload.answer，status="answered"，db.commit() 后返回该工单
    raise HTTPException(status_code=501, detail="作答接口待 03 阶段实现")
