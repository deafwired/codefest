from keybert import KeyBERT
import json
import requests


class API:
    def __init__(self):
        self.kw_model = KeyBERT()

    def keywords(self, prompt):
        keywords = self.kw_model.extract_keywords(
            prompt, keyphrase_ngram_range=(1, 1), stop_words="english", top_n=20
        )
        # Return only the keywords separated by commas
        return ",".join([word for word, score in keywords])

    def summary(self, prompt):
        # extract keywords using queryAi
        return self.keywords(prompt[:8000])

    def queryToKeywords(self, prompt):
        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "gemma:7b",
            "prompt": "From the given search query, generate a list of keywords for files which would be relevant to the query. The keywords should be separated by commas. \nQuery: " + prompt,
            "stream": False,
            "format": {
                "type": "object",
                "properties": {
                "keywords": {
                    "type": "array",
                    "items": {
                    "type": "string"
                    }
                }
                },
                "required": [
                "keywords"
                ]
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json().get("response", "No response recieved")
        else:
            return f"Error {response.status_code}: {response.text}"
