from abc import ABC, abstractmethod

class FrameworkDetector(ABC):

    @abstractmethod
    def detect(self, context):
        pass