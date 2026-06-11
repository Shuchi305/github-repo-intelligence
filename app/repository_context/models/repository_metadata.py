"""Repository metadata model"""

from dataclasses import dataclass

from .file_info import FileInfo

@dataclass
class RepositoryMetadata:
    name: str
    primary_language: str | None
    languages: dict[str, int]
    important_files: list[FileInfo]
    total_files: int
    total_lines: int
