from keybert import KeyBERT

class API:
    def __init__(self):
        self.kw_model = KeyBERT()
    
    def queryAi(self, prompt):
        keywords = self.kw_model.extract_keywords(
            prompt,
            keyphrase_ngram_range=(1, 1),
            stop_words="english",
            top_n=20
        )
        # Return only the keywords separated by commas
        return ','.join([word for word, score in keywords])
    
    def summary(self, prompt):
        # extract keywords using queryAi
        return self.queryAi(prompt[:8000])
