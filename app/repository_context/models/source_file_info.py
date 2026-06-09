"""Source file info model"""

from dataclasses import dataclass

class SourceFile:
    path: str
    language: str
    size_bytes: int