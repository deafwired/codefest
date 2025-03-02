import os
import sys

from Crypto.SelfTest.Cipher.test_OFB import file_name

from FileParser import FileParser
from util.api import API

class MetaData:
    def appendCSV(self, new_file_path, file_path, key_words):
        with open(new_file_path, "a") as file:
            file.write(file_path + ", ")
            file.write(key_words)
