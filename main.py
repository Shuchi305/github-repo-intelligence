"""Entrypoint for github-repo-intelligence"""

from multiprocessing import context

from app.repository_context.repository_context import RepositoryContext
from app.repository_scanner.scanner import RepositoryScanner
from app.framework_detection.engine import FrameworkDetectionEngine

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




if __name__ == "__main__":
    main()
