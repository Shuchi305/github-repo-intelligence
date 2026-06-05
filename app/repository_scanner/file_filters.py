"""File filters helper"""

from typing import List

def is_code_file(path: str) -> bool:
    return any(path.endswith(ext) for ext in ['.py', '.java', '.ts', '.js'])
