"""Django detector stub"""
from pathlib import Path
from .base_detector import FrameworkDetector
from ...repository_context.models.framework_info import FrameworkInfo
from ...repository_context.repository_context import RepositoryContext
class DjangoDetector(FrameworkDetector):
    def detect(self, context: RepositoryContext):

        requirements = context.get_important_file(
            "requirements.txt"
        )
        pyproject_toml = context.get_important_file(
            "pyproject.toml"
        )

        if not requirements and not pyproject_toml:
            return None

        content_parts = []

        if requirements:
            content_parts.append(Path(requirements.path).read_text())

        if pyproject_toml:
            content_parts.append(Path(pyproject_toml.path).read_text())


        content = "\n".join(content_parts)

        if "django" in content.lower():
            return FrameworkInfo(
                name="Django",
                confidence=0.95,
                version=None,
                evidence=["Dependency detected: django"]
            )

        return None
