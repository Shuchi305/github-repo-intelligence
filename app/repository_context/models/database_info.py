"""Database info model"""

from dataclasses import dataclass

@dataclass
class DatabaseInfo:
    database_type: str | None
    entities: list[str]
