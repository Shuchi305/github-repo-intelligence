"""Dependency extractor interface"""
from typing import Dict, List

class DependencyExtractor:
    def extract(self, repo_path: str) -> Dict[str, List[str]]:
        raise NotImplementedError()
