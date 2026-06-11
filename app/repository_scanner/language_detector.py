"""Language detection based on file extension"""


EXTENSION_LANGUAGE_MAP = {
    ".java": "Java",
    ".py": "Python",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".go": "Go",
    ".rb": "Ruby",
    ".cs": "C#",
    ".cpp": "C++",
    ".c": "C",
    ".php": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".scala": "Scala",
    ".rs": "Rust",
}


def detect_language(extension: str) -> str | None:
    return EXTENSION_LANGUAGE_MAP.get(extension.lower())