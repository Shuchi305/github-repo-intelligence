"""Dependency model"""

from dataclasses import dataclass

@dataclass
class Dependency:
    source: str
    target: str
    dependency_type: str  # e.g., "import", "inheritance", "function_call" , "extend", "implement", "use", "require", "include"
    line_number: int
    relative_level: int = 0  # For Python relative imports, e.g., from . import module (level=1), from .. import module (level=2)