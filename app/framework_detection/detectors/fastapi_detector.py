"""FastAPI detector stub"""
from pathlib import Path
from .base_detector import FrameworkDetector
from ...repository_context.models.framework_info import FrameworkInfo
from ...repository_context.repository_context import RepositoryContext
class FastAPIDetector(FrameworkDetector):

    def detect(self, context: RepositoryContext):

        requirements = context.get_important_file(
            "requirements.txt"
        )

        if not requirements:
            return None

        content = Path(
            requirements.path
        ).read_text()

        if "fastapi" in content.lower():
            return FrameworkInfo(
                name="FastAPI",
                confidence=0.95,
                version=None,
                evidence=["Dependency detected: fastapi"]
            )

        return None
