"""Entrypoint for github-repo-intelligence"""

from multiprocessing import context

from app.repository_context.repository_context import RepositoryContext
from app.repository_scanner.scanner import RepositoryScanner

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



if __name__ == "__main__":
    main()
