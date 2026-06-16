"""Entrypoint for github-repo-intelligence"""

from multiprocessing import context

from app.repository_context.repository_context import RepositoryContext
from app.repository_scanner.scanner import RepositoryScanner
from app.framework_detection.engine import FrameworkDetectionEngine
from app.symbol_indexing.symbol_indexing_engine import SymbolIndexingEngine
from app.dependency_graph.extractors.python_dependency_extractor import PythonDependencyExtractor
from app.dependency_graph.engine import DependencyGraphEngine

# TODO:
# Resolve relative/local imports into repository file paths.

def main():

    context = RepositoryContext(".")

    scanner = RepositoryScanner()

    scanner.scan(context)

    print("Files discovered:", len(context.source_files))
    print(context.source_files[0])
    print("Repository:", context.metadata.name)
    print("Files:", context.metadata.total_files)
    print("Languages:", context.metadata.languages)
    print("Primary Language:", context.metadata.primary_language)
    print("Important Files:", context.metadata.important_files)


    framework_engine = FrameworkDetectionEngine()

    frameworks = framework_engine.detect(context)
    print("Frameworks detected:", frameworks)

    print("\nDetected Frameworks:")

    for framework in frameworks:
        print(f"- {framework.name}")
        print(f"  Confidence: {framework.confidence}")
        print(f"  Version: {framework.version}")
        print(f"  Evidence: {framework.evidence}")

    engine = SymbolIndexingEngine()
    engine.build_symbol_index(context)

    print("\nExtracted Symbols:", len(context.symbols))
    for symbol in context.symbols:
        print(f"- {symbol.name} ({symbol.symbol_type}) in {symbol.file_path} at line {symbol.line_number}")

    extractor = PythonDependencyExtractor()

    for file_info in context.source_files:
        if file_info.language == "Python":
            deps = extractor.extract_dependencies(file_info.path)

            print(f"\n{file_info.path}")

            for dep in deps:
                print(f"  -> {dep.target}")

    dependency_engine = DependencyGraphEngine()
    dependency_engine.build(context)

    print(
        f"Dependencies: "
        f"{len(context.dependencies)}"
    )

    for dep in context.dependencies[:10]:
        print(dep)

if __name__ == "__main__":
    main()
