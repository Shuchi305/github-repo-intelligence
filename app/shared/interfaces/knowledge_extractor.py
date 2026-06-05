"""Knowledge extractor interface"""
from typing import Dict

class KnowledgeExtractor:
    def extract(self, repo_path: str) -> Dict:
        raise NotImplementedError()
