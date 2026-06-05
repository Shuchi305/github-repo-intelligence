"""Framework info model"""

from dataclasses import dataclass

@dataclass
class FrameworkInfo:
    name: str
    confidence: float
