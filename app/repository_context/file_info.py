"""File information model"""

from dataclasses import dataclass

@dataclass
class FileInfo:
    path: str
    size: int
    language: str | None = None
