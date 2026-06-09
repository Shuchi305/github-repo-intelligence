"""Repository scanner placeholder"""

import os

from ..repository_context.models.file_info import FileInfo
from .language_detector import detect_language
from .constants import IGNORED_DIRS
from ..repository_context.repository_context import RepositoryContext

class RepositoryScanner:

    def scan(self, context: RepositoryContext) -> None:

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
                file_info = FileInfo(
                    path=relative_path,
                    extension=extension,
                    size_bytes=size_bytes,
                    language=language
                )
                context.source_files.append(file_info)
