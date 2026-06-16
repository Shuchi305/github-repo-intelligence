
from abc import ABC, abstractmethod

from app.repository_context.models.symbol_info import SymbolInfo
from app.repository_context.models.file_info import FileInfo


class SymbolExtractor(ABC):

    @abstractmethod
    def extract_symbols(
        self,
        file_info: FileInfo
    ) -> list[SymbolInfo]:
        pass