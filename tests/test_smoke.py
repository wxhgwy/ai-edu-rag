"""冒烟测试：应用可导入、核心路由已注册。"""
from app.main import app


def test_app_imports() -> None:
    assert app.title == "AI_EDU RAG 知识库问答模块"


def test_core_routes_registered() -> None:
    paths = set(app.openapi()["paths"])
    assert "/health" in paths
    assert "/tickets" in paths
    assert "/practice/hello" in paths
