"""Repository scanner placeholder"""

import os

from ..repository_context.models.file_info import FileInfo
from .language_detector import detect_language
from .constants import IGNORED_DIRS
from ..repository_context.repository_context import RepositoryContext
from ..repository_context.models.repository_metadata import RepositoryMetadata
from .file_filters import is_important_file

class RepositoryScanner:

    def scan(self, context: RepositoryContext) -> None:

        language_counts = {}
        if context.metadata is None:
            context.metadata = RepositoryMetadata(
                name="repo_name",          # Replace with your actual name variable
                primary_language=None, # Set the first language found
                languages={},              # Initialize the empty dict
                important_files=[],
                total_files=0,
                total_lines=0,
            )

        for root, dirs, files in os.walk(context.repo_path):

            # Prevent os.walk from entering ignored directories
            dirs[:] = [
                d for d in dirs
                if d not in IGNORED_DIRS
            ]

            print(root)

            for file_name in files:
                full_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(
                    full_path,
                    context.repo_path
                )
                print("  ", relative_path)

                extension = os.path.splitext(file_name)[1]

                size_bytes = os.path.getsize(full_path)

                language = detect_language(extension)
                
                language_counts[language] = language_counts.get(language, 0) + 1
                context.metadata.total_files += 1
                file_info = FileInfo(
                    path=relative_path,
                    extension=extension,
                    size_bytes=size_bytes,
                    language=language
                )
                context.source_files.append(file_info)

                baseName = os.path.basename(file_name)
                if(is_important_file(baseName)):
                    context.metadata.important_files.append(file_info)

            

        if None in language_counts:
            del language_counts[None]
        if context.metadata.primary_language is None and language_counts:
            context.metadata.primary_language = max(
                language_counts,
                key=language_counts.get
            )
        context.metadata.languages = language_counts
