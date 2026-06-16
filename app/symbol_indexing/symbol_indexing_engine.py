"""Symbol indexing engine"""

from app.repository_context.repository_context import RepositoryContext

from .extractors.python_extractor import PythonSymbolExtractor

class SymbolIndexingEngine:

    def __init__(self):

        self.extractors = {
            "Python": PythonSymbolExtractor()
        }

    def build_symbol_index(
        self,
        context: RepositoryContext
    ):

        all_symbols = []

        for file_info in context.source_files:

            language = file_info.language

            extractor = self.extractors.get(language)

            if extractor is None:
                continue

            symbols = extractor.extract_symbols(file_info)

            all_symbols.extend(symbols)

        context.symbols = all_symbols