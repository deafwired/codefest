import os
import shutil
import subprocess
import threading
import webbrowser
from PySide6.QtCore import Qt, QFileInfo, QPoint
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QListWidget, QListWidgetItem, QFileIconProvider, QMenu
)
from PySide6.QtGui import QPixmap
from util.api import API
from search import QueryIndex
from util.fileTypes import FileTypeClassifier
from FileParser import FileParser
from Ingest import OrionIngest

class SearchResultWidget(QWidget):
    def __init__(self, text, file_path=None):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.thumbnail_label = QLabel()
        self.thumbnail_label.setFixedSize(64, 64)

        # Retrieve the system icon for the file, if possible.
        pixmap = None
        if file_path and os.path.exists(file_path):
            provider = QFileIconProvider()
            file_info = QFileInfo(file_path)
            icon = provider.icon(file_info)
            pixmap = icon.pixmap(64, 64)

        # If no icon was retrieved, use a generic image.
        if pixmap is None or pixmap.isNull():
            pixmap = QPixmap("./assets/generic.png")
            if not pixmap.isNull():
                pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        if pixmap and not pixmap.isNull():
            self.thumbnail_label.setPixmap(pixmap)
        else:
            self.thumbnail_label.setText("No Img")

        self.text_label = QLabel(text)
        self.text_label.setStyleSheet("font-size: 14px;")

        layout.addWidget(self.thumbnail_label)
        layout.addWidget(self.text_label)
        self.setLayout(layout)

class ResultListWidget(QListWidget):
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            item = self.currentItem()
            if item:
                # Emit the activated signal to open the file.
                self.itemActivated.emit(item)
            event.accept()
        else:
            super().keyPressEvent(event)

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search GUI")
        self.setGeometry(200, 200, 800, 500)

        layout = QVBoxLayout()

        # Header
        self.header = QLabel("Orion")
        self.header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.header)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        # When Enter is pressed in the search box, run the search.
        self.search_input.returnPressed.connect(self.perform_search)
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.perform_search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.result_list = ResultListWidget()
        # Use itemActivated so that Enter or double-click opens the file.
        self.result_list.itemActivated.connect(self.open_file)
        # Enable context menu for the list.
        self.result_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.result_list.customContextMenuRequested.connect(self.show_context_menu)
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    def perform_search(self):
        query = self.search_input.text()
        
        api = API()
        keywords = api.queryToKeywords(query)
        
        qi = QueryIndex()
        search_results = qi.generate_search(keywords, "data.csv")

        self.result_list.clear()

        for result in search_results:
            item = QListWidgetItem()
            widget = SearchResultWidget(result, file_path=result)
            item.setSizeHint(widget.sizeHint())
            item.setData(Qt.UserRole, result)
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, widget)

    def open_file(self, item):
        file_path = item.data(Qt.UserRole)
        if file_path and os.path.exists(file_path):
            print(f"Opening file: {file_path}")  # Debug output
            if os.name == 'nt':  # Windows
                os.startfile(file_path)
            elif os.name == 'posix':  # macOS and Linux
                try:
                    subprocess.run(["xdg-open", file_path], check=True)  # Linux
                except FileNotFoundError:
                    try:
                        subprocess.run(["open", file_path], check=True)  # macOS
                    except FileNotFoundError:
                        webbrowser.open(file_path)  # Fallback
            else:
                webbrowser.open(file_path)  # Fallback for unknown OS
        else:
            print(f"File not found: {file_path}")

    def show_context_menu(self, pos):
        item = self.result_list.itemAt(pos)
        if item is not None:
            menu = QMenu(self)
            open_folder_action = menu.addAction("Open Folder")
            action = menu.exec_(self.result_list.viewport().mapToGlobal(pos))
            if action == open_folder_action:
                self.open_folder(item)

    def open_folder(self, item):
        file_path = item.data(Qt.UserRole)
        if file_path and os.path.exists(file_path):
            folder = os.path.dirname(file_path)
            print(f"Opening folder: {folder}")  # Debug output
            if os.name == 'nt':  # Windows: select file in Explorer
                subprocess.run(["explorer", "/select,", file_path])
            elif os.name == 'posix':
                try:
                    subprocess.run(["open", "-R", file_path], check=True)  # macOS: reveal in Finder
                except Exception:
                    subprocess.run(["xdg-open", folder])  # Linux fallback
            else:
                webbrowser.open(folder)
        else:
            print(f"Folder not found for file: {file_path}")

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

def main():
    # Start the ingestion process in a separate thread.
    isOllamaInstalled()
    ingest = OrionIngest()
    ingest.handleFile = my_custom_handle_file
    ingest_thread = threading.Thread(target=ingest.start, daemon=True)
    ingest_thread.start()
    print("Ingest is running in a separate thread. Main script continues executing.")

    # Start the GUI.
    app = QApplication([])
    window = SearchApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()