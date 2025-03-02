from FileParser import FileParser
from util.api import API
import os

if __name__ == "__main__":
    for filename in os.listdir("./testFiles/"):
        path = os.path.join("./testFiles", filename)
        fp = FileParser()
        api = API()
        summary = api.summary(fp.extract_text(path))
        print(f"{filename}: {summary}")
        print(f"{filename} new name: {api.name(summary)}")
