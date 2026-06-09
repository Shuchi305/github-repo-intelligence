"""Language detection based on file extension"""
from ..repository_context.models.language import Language


EXTENSION_LANGUAGE_MAP = {
    ".java": Language.JAVA,
    ".py": Language.PYTHON,
    ".ts": Language.TYPESCRIPT,
    ".tsx": Language.TYPESCRIPT,
}


def detect_language(extension: str) -> Language | None:
    return EXTENSION_LANGUAGE_MAP.get(extension.lower())