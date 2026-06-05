"""Symbol extractor interface"""
from typing import List, Dict

class SymbolExtractor:
    def extract(self, file_path: str) -> List[Dict]:
        raise NotImplementedError()
