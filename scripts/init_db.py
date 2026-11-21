"""初始化数据库：确认 vector 扩展就绪，并按 ORM 模型建表。

在项目根目录执行：
    venv\Scripts\python scripts\init_db.py

换机器复现时：先装好 PostgreSQL 16 + pgvector、配好 `.env`，再跑本脚本。
"""
import sys
from pathlib import Path

# 允许从 scripts/ 目录直接运行时找到项目根下的 packages 包
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from packages.common.database import Base, engine  # noqa: E402
from packages.rag.models import Ticket  # noqa: E402,F401  导入以注册模型到 metadata


def main() -> None:
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()

    Base.metadata.create_all(bind=engine)
    print("INIT_DB_OK：vector 扩展就绪，数据表已建（tickets 等）")


if __name__ == "__main__":
    main()
