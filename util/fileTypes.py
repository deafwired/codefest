import sys

class FileTypeClassifier:
    def __init__(self):
        """Initialize the file type dictionary with categories and support status."""
        self.fileTypes = {
            "Documents": {".txt": True, ".pdf": True, ".docx": True, ".doc": True, ".odt": False, ".rtf": False, ".md": True},
            "Spreadsheets": {".xlsx": True, ".xls": True, ".csv": True, ".ods": False},
            "Presentations": {".pptx": True, ".ppt": True, ".odp": False},
            "Photos": {".jpg": False, ".jpeg": False, ".png": False, ".gif": False, ".bmp": False, ".tiff": False, ".svg": False, ".webp": False},
            "Videos": {".mp4": False, ".mkv": False, ".avi": False, ".mov": False, ".flv": False, ".wmv": False, ".webm": False},
            "Audio": {".mp3": False, ".wav": False, ".flac": False, ".aac": False, ".ogg": False, ".m4a": False},
            "Archives": {".zip": False, ".rar": False, ".tar": False, ".gz": False, ".7z": False, ".bz2": False},
            "Executables": {".exe": False, ".bat": False, ".sh": False, ".msi": False, ".apk": False, ".app": False, ".deb": False, ".rpm": False},
            "Code Files": {".py": False, ".js": False, ".html": False, ".css": False, ".java": False, ".c": False, ".cpp": False, ".cs": False, ".php": False, ".go": False, ".swift": False, ".rb": False, ".ts": False},
            "Database": {".sql": False, ".db": False, ".sqlite": False, ".mdb": False, ".accdb": False},
            "System Files": {".dll": False, ".sys": False, ".ini": False, ".cfg": False, ".log": False},
            "Fonts": {".ttf": False, ".otf": False, ".woff": False, ".woff2": False},
            "Disk Images": {".iso": False, ".img": False, ".vmdk": False},
        }

        # Flatten the structure for quick lookup
        self.extensionMap = {
            ext: {"category": category, "supported": supported}
            for category, extensions in self.fileTypes.items()
            for ext, supported in extensions.items()
        }

    def getFileInfo(self, extension):
        """Returns the category and support status of a given file extension."""
        return self.extensionMap.get(extension, {"category": "Unknown", "supported": False})