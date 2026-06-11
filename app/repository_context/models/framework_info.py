"""Framework info model"""

from dataclasses import dataclass

@dataclass
class FrameworkInfo:
    name: str
    version: str | None
    confidence: float
    evidence: list[str]
