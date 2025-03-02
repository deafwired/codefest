import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QListWidget, QListWidgetItem, QFileIconProvider
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QFileInfo
from util.api import API
from search import QueryIndex

class SearchResultWidget(QWidget):
    def __init__(self, text, file_path=None):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.thumbnail_label = QLabel()
        self.thumbnail_label.setFixedSize(64, 64)
        self.thumbnail_label.setStyleSheet(
            ""
        )

        # Attempt to retrieve the system icon for the file.
        pixmap = None
        if file_path and os.path.exists(file_path):
            provider = QFileIconProvider()
            file_info = QFileInfo(file_path)
            icon = provider.icon(file_info)
            pixmap = icon.pixmap(64, 64)

        # if no icon could be retrieved, use the generic image.
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
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.perform_search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.result_list = QListWidget()
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
            print(result)
            item.setSizeHint(widget.sizeHint())
            self.result_list.addItem(item)
            self.result_list.setItemWidget(item, widget)

import cProfile

def main():
    app = QApplication([])
    window = SearchApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    cProfile.run("main()", "search_profile.prof", sort="cumtime")