"""Repository metadata model"""

from dataclasses import dataclass

@dataclass
class RepositoryMetadata:
    name: str
    primary_language: str | None
    languages: list[str]
    total_files: int
    total_lines: int
