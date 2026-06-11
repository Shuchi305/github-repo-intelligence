"""Framework detection engine"""

from abc import ABC, abstractmethod
# from app.repository_context.models.framework_info import FrameworkInfo
# from app.repository_context.repository_context import RepositoryContext
# from .detectors.base_detector import FrameworkDetector
from .detectors.fastapi_detector import FastAPIDetector
from .detectors.django_detector import DjangoDetector
from .detectors.spring_boot_detector import SpringBootDetector

class FrameworkDetectionEngine:

    def __init__(self):

        self.detectors = [
            FastAPIDetector(),
            DjangoDetector(),
            SpringBootDetector(),
        ]

    def detect(self, context):

        frameworks = []

        for detector in self.detectors:

            result = detector.detect(context)

            if result:
                frameworks.append(result)

        return frameworks
