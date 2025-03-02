from util.fileTypes import FileTypeClassifier

def getCategory(filePath):
    classifier = FileTypeClassifier()
    fileExtension = "." + filePath.split('.')[-1].lower()
    fileInfo = classifier.getFileInfo(fileExtension)
    
    if not fileInfo["supported"]:
        return None
    
    category = fileInfo["category"]

    return category

def moveFile(filePath, category):
    # Placeholder
    if category is None:
        print(f"Moving {filePath} to Add-To-Orion/unsupported.")
        return
    print(f"Moving {filePath} to {category} folder.")

if __name__ == "__main__":
    # Example usage
    filePath = "example.txt"
    moveFile(filePath, getCategory(filePath))
    
    filePath = "example.unsupported"
    moveFile(filePath, getCategory(filePath))