"""File filters helper"""

from typing import List
from .constants import IMPORTANT_FILES

def is_important_file(baseName: str) -> bool:
    return baseName in IMPORTANT_FILES
