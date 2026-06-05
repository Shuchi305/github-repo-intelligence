"""Analysis response contract"""

from dataclasses import dataclass

@dataclass
class AnalysisResponse:
    summary: str
    details: dict
