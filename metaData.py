import os
import sys

from Crypto.SelfTest.Cipher.test_OFB import file_name

from fileParser import FileParser
from util.api import API

def appendCSV(new_file_path, file_path, key_words):
    with open(new_file_path, "a") as file:
        file.write(file_path + ", ")
        file.write(key_words)

    return file

if __name__ == "__main__":
    fp = FileParser()
    api = API()

    file_path = fp.get_file_path()
    print(file_path)
    key_words = api.summary(fp.extract_text(file_path))

    output = appendCSV("data.csv", file_path, key_words)