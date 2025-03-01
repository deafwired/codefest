import os
import shutil
import subprocess
from collections import defaultdict
from util.fileTypes import FileTypeClassifier


def isOllamaInstalled():
# Check if Ollama is installed and print its version.
    if shutil.which("ollama") is not None:
        try:
            result = subprocess.run(["ollama", "--version"], capture_output=True, text=True, check=True)
            print("Ollama is installed. Version:", result.stdout.strip())
            return True
        except subprocess.CalledProcessError:
            print("Ollama not installed.")
            return False
    else:
        print("Ollama is not installed.")
        return False
    
if __name__ == "__main__":
    isOllamaInstalled()
