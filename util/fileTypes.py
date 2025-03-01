from collections import defaultdict

fileTypes = defaultdict(lambda: "Unknown", {
    ext: category
    for category, extensions in {
        "Documents": [".txt", ".pdf", ".docx", ".doc", ".odt", ".rtf", ".md"],
        "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
        "Presentations": [".pptx", ".ppt", ".odp"],
        "Photos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
        "Executables": [".exe", ".bat", ".sh", ".msi", ".apk", ".app", ".deb", ".rpm"],
        "Code Files": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".php", ".go", ".swift", ".rb", ".ts"],
        "Database": [".sql", ".db", ".sqlite", ".mdb", ".accdb"],
        "System Files": [".dll", ".sys", ".ini", ".cfg", ".log"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Disk Images": [".iso", ".img", ".vmdk"],
    }.items()
    for ext in extensions
})

def getFileCategory(extension):
    """Returns the category for a given file extension."""
    return file_types[extension]