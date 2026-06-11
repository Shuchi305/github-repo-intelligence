"""File information model"""

from dataclasses import dataclass


@dataclass
class FileInfo:
    path: str
    extension: str
    size_bytes: int
    language: str | None = None