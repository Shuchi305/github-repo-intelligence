"""Repository storage helpers"""

class RepositoriesStore:
    def __init__(self):
        self._repos = {}

    def add(self, metadata):
        self._repos[metadata.name] = metadata
