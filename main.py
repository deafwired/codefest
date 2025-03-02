from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from util.api import API
from search import QueryIndex

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
            self.result_list.addItem(result)

if __name__ == "__main__":
    app = QApplication([])
    window = SearchApp()
    window.show()
    app.exec()