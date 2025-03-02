from fileinput import filename
from search import QueryIndex
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QListWidget

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search GUI")
        self.setGeometry(200, 200, 800, 500)

        # Layout
        layout = QVBoxLayout()

        # Header
        self.header = QLabel("Orion")
        self.header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.header)

        # Search Bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.perform_search)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # Search Results
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    def perform_search(self, filename, query):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = SearchApp()
    window.show()
    app.exec()
