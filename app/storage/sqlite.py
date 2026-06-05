"""SQLite storage helper placeholder"""

import sqlite3

class SQLiteStorage:
    def __init__(self, path: str):
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)
