from FileParser import FileParser
from util.api import API
import os
import json

if __name__ == "__main__":
    for filename in os.listdir("./testFiles/"):
        path = os.path.join("./testFiles", filename)
        fp = FileParser()
        api = API()
        # summary = api.summary(fp.extract_text(path))
        # print(f"{filename}: {summary}")
        # print(f"{filename} new name: {api.name(summary)}")
        query = "Tax docs" # Test query
        keywords = api.queryToKeywords(query) # Turn query into keywords
        parse = json.loads(keywords)
        singleWords = [] 
        #Keywords from AI can be multiple words, parse them into single words and remove duplicates
        for key in parse["keywords"]:
            for word in key.split(" "):
                singleWords.append(word)
        singleWords = list(set(singleWords))
        
        print(f"{singleWords}")