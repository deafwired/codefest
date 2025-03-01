import os
import time

def checkOrCreateFolder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
        print(f"Folder created: {folderPath}")
    else:
        print(f"Folder already exists: {folderPath}")

def queryFolderContents(folderPath):
    while True:
        print(f"Querying contents of folder: {folderPath}")
        for filename in os.listdir(folderPath):
            filePath = os.path.join(folderPath, filename)
            if os.path.isfile(filePath):
                print(f"Found file: {filePath}")
        time.sleep(60)  # Run the task every 60 seconds

if __name__ == "__main__":
    documentsFolder = os.path.expanduser("~/Documents")
    addToOrionFolder = os.path.join(documentsFolder, "Add to Orion")

    checkOrCreateFolder(addToOrionFolder)
    queryFolderContents(addToOrionFolder)