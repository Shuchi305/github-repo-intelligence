"""Database info model"""

from dataclasses import dataclass

@dataclass
class DatabaseInfo:
    engine: str
    connection_string: str | None = None
