"""API info model"""

from dataclasses import dataclass
from ..models.api_endpoint import ApiEndpoint

@dataclass
class ApiInfo:
    endpoints: list[ApiEndpoint]
