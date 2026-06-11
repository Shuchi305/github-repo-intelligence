"""React detector stub"""
from pathlib import Path
from .base_detector import FrameworkDetector
from ...repository_context.models.framework_info import FrameworkInfo
from ...repository_context.repository_context import RepositoryContext

class ReactDetector(FrameworkDetector):
    def detect(self, context: RepositoryContext):

        package_json = context.get_important_file(
            "package.json"
        )

        if not package_json:
            return None

        content = Path(
            package_json.path
        ).read_text()

        if "react" in content.lower():
            return FrameworkInfo(
                name="React",
                confidence=0.95,
                version=None,
                evidence=["Dependency detected: react"]
            )

        return None

