"""Symbol extractor interface"""
from abc import ABC, abstractmethod
from typing import List, Dict

from ...repository_context.models.symbol_info import SymbolInfo

class SymbolExtractor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> List[SymbolInfo]:
        pass
