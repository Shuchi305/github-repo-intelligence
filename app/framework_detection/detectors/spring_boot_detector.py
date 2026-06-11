"""Spring Boot detector stub"""
from pathlib import Path
from .base_detector import FrameworkDetector
from ...repository_context.models.framework_info import FrameworkInfo
from ...repository_context.repository_context import RepositoryContext

class SpringBootDetector(FrameworkDetector):
    def detect(self, context: RepositoryContext):

        requirements = context.get_important_file(
            "pom.xml"
        )
        build_gradle = context.get_important_file(
            "build.gradle"
        )
        build_gradle_kts = context.get_important_file(
            "build.gradle.kts"      
        )

        if not requirements and not build_gradle and not build_gradle_kts:
            return None
        content_parts = []

        if requirements:
            content_parts.append(Path(requirements.path).read_text())

        if build_gradle:
            content_parts.append(Path(build_gradle.path).read_text())

        if build_gradle_kts:
            content_parts.append(Path(build_gradle_kts.path).read_text())


        content = "\n".join(content_parts)

        if "spring-boot-starter" in content.lower():
            return FrameworkInfo(
                name="Spring Boot",
                confidence=0.95,
                version=None,
                evidence=["Dependency detected: spring-boot-starter"]
            )

        return None

