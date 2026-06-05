"""Symbol information model"""

from dataclasses import dataclass

@dataclass
class SymbolInfo:
    name: str
    kind: str
    location: str
