"""API Endpoint model"""

from dataclasses import dataclass

@dataclass
class ApiEndpoint:
    path: str
    method: str