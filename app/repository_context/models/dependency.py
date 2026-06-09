"""Dependency model"""

from dataclasses import dataclass

@dataclass
class Dependency:
    source: str
    target: str
    dependency_type: str  # e.g., "import", "inheritance", "function_call" , "extend", "implement", "use", "require", "include"