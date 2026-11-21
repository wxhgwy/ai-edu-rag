"""应用配置：从项目根目录 `.env` 读取 LLM 与数据库参数。

- 真实密钥只在本地 `.env`（已被 .gitignore 忽略），本文件不硬编码任何密钥。
- 切官方 DashScope / 本地 Qwen 只改 `.env`，业务代码不动。
"""
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# 项目根目录（packages/common/config.py -> common -> packages -> 根目录）
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # 云端 LLM（OpenAI 兼容接口）
    llm_base_url: str
    llm_model: str
    dashscope_api_key: str

    # PostgreSQL 16
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

    @property
    def database_url(self) -> str:
        """SQLAlchemy 连接串（psycopg2 驱动）。"""
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


@lru_cache
def get_settings() -> Settings:
    """配置单例，避免重复读 .env。"""
    return Settings()
