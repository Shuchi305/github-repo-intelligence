"""Symbol information model"""

from dataclasses import dataclass

@dataclass
class SymbolInfo:
    name: str
    symbol_type: str
    file_path: str
    line_number: int
