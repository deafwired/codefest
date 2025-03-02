import os
import sys

from Crypto.SelfTest.Cipher.test_OFB import file_name

from FileParser import FileParser
from util.api import API

class MetaData:
    def appendCSV(self, file_path, key_words):
        api = API()

        with open("data.csv", "a") as file:
            file_metadata = api.queryToKeywords(file_path)
            file.write(file_path + ",")
            file.write(key_words + ",")
            file.write(file_metadata)
            file.write("\n")
