"""Repository scanner placeholder"""

import os

class Scanner:
    def __init__(self, root: str):
        self.root = root

    def walk(self):
        for dirpath, dirnames, filenames in os.walk(self.root):
            yield dirpath, filenames
