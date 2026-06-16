"""Python dependency extractor stub"""

import ast
from pathlib import Path

from app.shared.interfaces.dependency_extractor import DependencyExtractor
from app.repository_context.models.dependency import Dependency

class PythonDependencyExtractor(DependencyExtractor):

    def extract_dependencies(self, file_path: str) -> list[Dependency]:
        """
        Extract import dependencies from a Python file using AST.

        Supports:
        - import module
        - import module as alias
        - from module import symbol

        Ignores:
        - dynamic imports
        - dependency usage analysis
        - relative import resolution
        """

        with open(file_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        tree = ast.parse(source_code)

        dependencies: list[Dependency] = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    dependencies.append(
                        Dependency(
                            source=str(Path(file_path)),
                            target=alias.name,
                            dependency_type="import",
                            line_number=node.lineno
                        )
                    )

            elif isinstance(node, ast.ImportFrom):

                if node.module is None:
                    continue

                dependencies.append(
                    Dependency(
                        source=str(Path(file_path)),
                        target=node.module,
                        dependency_type="from_import",
                        relative_level=node.level,
                        line_number=node.lineno
                    )
                )

        return dependencies