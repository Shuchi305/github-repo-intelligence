"""Python symbol extractor stub"""

import ast
from typing import List

from app.repository_context.models.file_info import FileInfo
from app.repository_context.models.symbol_info import SymbolInfo
from .base_extractor import SymbolExtractor


class PythonSymbolExtractor(SymbolExtractor):

    def extract_symbols(
        self,
        file_info: FileInfo
    ) -> List[SymbolInfo]:

        symbols = []

        try:
            with open(file_info.path, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    symbols.append(
                        SymbolInfo(
                            name=node.name,
                            symbol_type="class",
                            file_path=file_info.path,
                            line_number=node.lineno,
                            language="python"
                        )
                    )

                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    symbols.append(
                        SymbolInfo(
                            name=node.name,
                            symbol_type="function",
                            file_path=file_info.path,
                            line_number=node.lineno,
                            language="python"
                        )
                    )

        except Exception as e:
            print(f"Failed to parse {file_info.path}: {e}")

        return symbols