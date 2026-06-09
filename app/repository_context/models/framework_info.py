"""Framework info model"""

from dataclasses import dataclass

@dataclass
class FrameworkInfo:
    name: str
    version: str | None
    evidence_files: list[str]
