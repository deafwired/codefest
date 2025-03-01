from fileParser import FileParser
from util.api import API
import os

if __name__ == "__main__":
    for filename in os.listdir("./testFiles/"):
        path = os.path.join("./testFiles",filename)
        fp = FileParser()
        api = API()
        print(f"{filename}: {api.summary(fp.extract_text(path))}")
