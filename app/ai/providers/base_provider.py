"""Base AI provider interface"""

class BaseProvider:
    def send(self, prompt: str):
        raise NotImplementedError()
