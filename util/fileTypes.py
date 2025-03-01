import sys

class FileTypeClassifier:
    def __init__(self):
        """Initialize the file type dictionary with categories and their support status."""
        self.fileTypes = {
            "Documents": { "supported": True, "extensions": [".txt", ".pdf", ".docx", ".doc", ".odt", ".rtf", ".md"] },
            "Spreadsheets": { "supported": True, "extensions": [".xlsx", ".xls", ".csv", ".ods"] },
            "Presentations": { "supported": True, "extensions": [".pptx", ".ppt", ".odp"] },
            "Photos": { "supported": True, "extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"] },
            "Videos": { "supported": True, "extensions": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm"] },
            "Audio": { "supported": True, "extensions": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"] },
            "Archives": { "supported": False, "extensions": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"] },
            "Executables": { "supported": False, "extensions": [".exe", ".bat", ".sh", ".msi", ".apk", ".app", ".deb", ".rpm"] },
            "Code Files": { "supported": True, "extensions": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".php", ".go", ".swift", ".rb", ".ts"] },
            "Database": { "supported": False, "extensions": [".sql", ".db", ".sqlite", ".mdb", ".accdb"] },
            "System Files": { "supported": False, "extensions": [".dll", ".sys", ".ini", ".cfg", ".log"] },
            "Fonts": { "supported": True, "extensions": [".ttf", ".otf", ".woff", ".woff2"] },
            "Disk Images": { "supported": False, "extensions": [".iso", ".img", ".vmdk"] },
        }

        # Create a flattened extension lookup for quick access
        self.extensionMap = {
            ext: {"category": category, "supported": info["supported"]}
            for category, info in self.fileTypes.items()
            for ext in info["extensions"]
        }

    def getFileInfo(self, extension):
        """Returns the category and support status of a given file extension."""
        return self.extensionMap.get(extension, {"category": "Unknown", "supported": False})