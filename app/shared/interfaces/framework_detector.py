"""Framework detector interface"""
from typing import Dict

class FrameworkDetector:
    def detect(self, repo_path: str) -> Dict[str, float]:
        raise NotImplementedError()
