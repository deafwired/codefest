Heres how to use the classifer

from util.fileTypes import FileTypeClassifier
classifier = FileTypeClassifier()

fileExtension = ".cpp"
fileInfo = classifier.getFileInfo(fileExtension)

print(f"File extension '{fileExtension}' belongs to category: {fileInfo['category']}, Supported: {fileInfo['supported']}")

should print File extension '.cpp' belongs to category: CodeFiles, Supported: True
