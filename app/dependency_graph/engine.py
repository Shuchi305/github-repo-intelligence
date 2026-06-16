"""Dependency graph engine"""

from app.repository_context.repository_context import RepositoryContext
from app.dependency_graph.extractors.python_dependency_extractor import PythonDependencyExtractor
class DependencyGraphEngine:

    def __init__(self):
        self.python_extractor = PythonDependencyExtractor()

    def build(self, repository_context: RepositoryContext):

        for file_info in repository_context.source_files:

            if file_info.language != "Python":
                continue

            dependencies = self.python_extractor.extract_dependencies(
                file_info.path
            )

            repository_context.dependencies.extend(dependencies)