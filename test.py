from FileParser import FileParser
from util.api import API
import os
import json
from search import QueryIndex

if __name__ == "__main__":
    # for filename in os.listdir("./testFiles/"):
    fp = FileParser()
    api = API()
    # summary = api.summary(fp.extract_text(path))
    # print(f"{filename}: {summary}")
    # print(f"{filename} new name: {api.name(summary)}")
    query = "I want a file that contains passwords"  # Test query
    keywords = api.queryToKeywords(query)
    print(keywords)
    qi = QueryIndex()
    search_results = qi.generate_search(keywords, "data.csv")
    print(search_results)

    # print(f"{keywords}")
