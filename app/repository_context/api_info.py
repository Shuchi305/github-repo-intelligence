"""API info model"""

from dataclasses import dataclass

@dataclass
class APIInfo:
    endpoint: str
    methods: list
