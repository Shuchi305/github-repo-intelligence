"""Repository metadata model"""

from dataclasses import dataclass

@dataclass
class RepositoryMetadata:
    name: str
    path: str
    language: str | None = None
