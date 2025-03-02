import os
import sys

from FileParser import FileParser
from util.api import API

class MetaData:
    def appendCSV(self, file_path, key_words):
        api = API()

        if isinstance(key_words, list):
            key_words = ", ".join(key_words)
            
        file_metadata = api.queryToKeywords(file_path)
        if isinstance(file_metadata, list):
            file_metadata = ", ".join(file_metadata)

        with open("data.csv", "a") as file:
            file.write(file_path + ",")
            file.write(key_words + ",")
            file.write(file_metadata)
            file.write("\n")