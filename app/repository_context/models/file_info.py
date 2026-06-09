"""File information model"""

from dataclasses import dataclass

from  ..models.language import Language

@dataclass
class FileInfo:
    path: str
    extension: str
    size_bytes: int
    language: Language | None = None