"""Symbol information model"""

from dataclasses import dataclass
from enum import Enum

class SymbolType(Enum):
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    INTERFACE = "interface"

@dataclass
class SymbolInfo:
    name: str
    symbol_type: SymbolType
    file_path: str
    line_number: int
    language: str
