import requests
import json
import os

class API:
    def __init__(self):
        self.host = "http://localhost:11434"
        self.model = "gemma:2b"
    def queryAi(self, prompt):
        url = f"{self.host}/api/generate"
        headers = { "Content-Type": "application/json" }
        payload = {
            "model": self.model,
            "prompt": prompt,
            # "format": "json",
            "stream": False,
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            return response.json().get("response", "No response received")
        else:
            return f"Error {response.status_code}: {response.text}"
    def summary(self, prompt):
        return self.queryAi("Summarize the following text in one concise sentence:\n" + prompt[:8000])
