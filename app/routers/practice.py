"""第 1 周练习：HTTP 与 FastAPI（内存版，数据重启即丢）。

对应每日任务第 1 周：
- GET 查询参数 / 路径参数
- Pydantic 请求体 + POST
- HTTPException 异常
- async 异步接口
- 路由拆分（本文件单独一个路由，在 main.py 挂载）

第 2 周再接 PostgreSQL，这里不碰数据库。
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/practice", tags=["practice-第1周练习"])

# ---------- 内存存储（练习用，服务重启即清空） ----------
_notes: list[dict] = []
_next_id: int = 1

_items: dict[int, str] = {1: "向量检索", 2: "混合检索", 3: "重排序"}


# ---------- Pydantic 请求 / 响应模型 ----------
class NoteCreate(BaseModel):
    """新建笔记的请求体：前端传 JSON，字段非空、长度受限。"""

    title: str = Field(..., min_length=1, max_length=100, description="笔记标题")
    content: str = Field(..., min_length=1, description="笔记内容")


class NoteOut(BaseModel):
    """笔记响应体。"""

    id: int
    title: str
    content: str


# ---------- 1. GET 查询参数 ----------
@router.get("/hello")
def hello(name: str = "同学"):
    """GET /practice/hello?name=张三 -> 问候语；name 是查询参数，可缺省。"""
    return {"message": f"你好，{name}！这是第 1 周练习接口。"}


# ---------- 2. GET 路径参数 ----------
@router.get("/items/{item_id}")
def get_item(item_id: int):
    """GET /practice/items/1 -> 按路径里的 id 查商品；找不到抛 404。"""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="商品不存在")
    return {"item_id": item_id, "name": _items[item_id]}


# ---------- 3. 笔记：查列表 ----------
@router.get("/notes")
def list_notes():
    """GET /practice/notes -> 返回全部内存笔记。"""
    return _notes


# ---------- 4. 笔记：查单个 ----------
@router.get("/notes/{note_id}")
def get_note(note_id: int):
    """GET /practice/notes/1 -> 按 id 查单条；找不到 404。"""
    for note in _notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="笔记不存在")


# ---------- 5. 笔记：新增（POST + 请求体 + async） ----------
@router.post("/notes", response_model=NoteOut)
async def create_note(payload: NoteCreate):
    """POST /practice/notes -> 接收 JSON 请求体，写入内存列表。

    用 async def 示范异步接口；当前没有阻塞 IO，效果和普通 def 一样。
    """
    global _next_id
    note = {"id": _next_id, "title": payload.title, "content": payload.content}
    _notes.append(note)
    _next_id += 1
    return note


# ---------- 6. TODO：删除（第 1 周自己补） ----------
@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """TODO(第1周练习)：按 id 从 _notes 删除；找不到抛 404；成功返回删除后的列表或成功提示。"""
    raise HTTPException(status_code=501, detail="删除接口待自己实现")
