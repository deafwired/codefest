import os
import shutil
import subprocess
import threading
from collections import defaultdict
from util.fileTypes import FileTypeClassifier
from util.api import API
from FileParser import FileParser
from Ingest import OrionIngest


def isOllamaInstalled():
    # Check if Ollama is installed and print its version.
    if shutil.which("ollama") is not None:
        try:
            result = subprocess.run(
                ["ollama", "--version"], capture_output=True, text=True, check=True
            )
            print("Ollama is installed. Version:", result.stdout.strip())
            return True
        except subprocess.CalledProcessError:
            print("Ollama not installed.")
            return False
    else:
        print("Ollama is not installed.")
        return False


def my_custom_handle_file(file_path):
    fp = FileParser()
    api = API()
    split = os.path.splitext(file_path)
    extension = split[-1]
    classify = FileTypeClassifier()
    content = fp.extract_text(file_path)
    keywords = api.summary(content)
    newPath = classify.getFileInfo(extension)
    return os.path.join(newPath["category"], os.path.basename(file_path)), keywords


if __name__ == "__main__":
    isOllamaInstalled()
    ingest = OrionIngest()
    ingest.handleFile = my_custom_handle_file

    ingest_thread = threading.Thread(target=ingest.start, daemon=True)
    ingest_thread.start()

    print("Ingest is running in a separate thread. Main script continues executing.")

    input("Press Enter to exit...")
