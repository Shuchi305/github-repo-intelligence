"""OpenAI provider stub"""

class OpenAIProvider:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def send(self, prompt: str):
        return {"response": ""}
