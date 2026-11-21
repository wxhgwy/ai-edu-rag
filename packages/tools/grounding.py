"""落地性检查：标出回答中缺少知识库依据的句子。

任务书要求复用 packages/tools 检查回答、标出低支撑句子。
打分策略在 04 模块实现，这里先固定接口，避免后续改动调用方。
"""
from dataclasses import dataclass


@dataclass
class SupportCheckResult:
    """单句支撑检查结果。"""

    sentence: str
    supported: bool
    score: float


def check_support(
    answer: str, contexts: list[str], threshold: float = 0.5
) -> list[SupportCheckResult]:
    """逐句评估回答是否被 contexts 支撑。

    占位实现：04 模块接入嵌入相似度后替换。
    """
    raise NotImplementedError("落地性检查将在 04 模块实现")
