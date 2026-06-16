"""Dependency extractor interface"""
from abc import ABC, abstractmethod

class DependencyExtractor(ABC):

    @abstractmethod
    def extract_dependencies(self, file_path: str):
        pass
