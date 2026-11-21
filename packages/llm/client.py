"""统一 LLM 抽象层。

- 所有对大模型的调用只走本模块，业务代码不直接 import openai。
- base_url / 模型名 / Key 全部来自 `.env`，切换官方 DashScope、第三方中转或本地
  Qwen（Ollama 等 OpenAI 兼容服务）只改配置，不动这里的调用逻辑。
- 本地不跑 7B 大模型；4GB 显存只跑嵌入与重排小模型，大模型走云端 API。
"""
from functools import lru_cache

from openai import OpenAI

from packages.common.config import get_settings


class LLMClient:
    """OpenAI 兼容客户端封装（通义千问 / 中转 / 本地 Qwen 均可对接）。"""

    def __init__(self) -> None:
        settings = get_settings()
        self.model = settings.llm_model
        self._client = OpenAI(
            api_key=settings.dashscope_api_key,
            base_url=settings.llm_base_url,
        )

    def chat(self, prompt: str, temperature: float = 0.1) -> str:
        """单轮问答，返回模型文本。后续 04 模块再补流式输出方法。"""
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return resp.choices[0].message.content or ""


@lru_cache
def get_llm_client() -> LLMClient:
    """LLM 客户端单例。"""
    return LLMClient()
