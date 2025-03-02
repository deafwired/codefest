import os
import sys
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from util.fileTypes import FileTypeClassifier
from metaData import MetaData


class OrionIngest:
    def __init__(self):
        documents_folder = Path.home() / "Documents"
        self.metadata = MetaData()
        self.orion_folder = documents_folder / "Orion"
        self.add_to_orion_folder = documents_folder / "Add to Orion"

        self._setup_folders()

    def _setup_folders(self):
        for folder in [self.orion_folder, self.add_to_orion_folder]:
            if not folder.exists():
                print(f"{folder} does not exist. Creating it.")
                try:
                    folder.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    logging.error(f"Error creating folder {folder}: {e}")
                    sys.exit(1)
            else:
                print(f"{folder} exists.")
        fileTypes = FileTypeClassifier().getFileTypes()
        for key in fileTypes.keys():
            folder = self.orion_folder / key
            if not folder.exists():
                print(f"{folder} does not exist. Creating it.")
                try:
                    folder.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    logging.error(f"Error creating folder {folder}: {e}")
                    sys.exit(1)
            else:
                print(f"{folder} exists.")

    def handleFile(self, file_path):
        print(f"Handling file: {file_path}")

    class OrionEventHandler(FileSystemEventHandler):
        def __init__(self, ingest_instance):
            self.ingest_instance = ingest_instance

        def on_created(self, event):
            path, keywords = self.ingest_instance.handleFile(event.src_path)
            self.updateFile(event.src_path, path, keywords)

    def start(self):
        # Process existing files in the "Add to Orion" folder
        for item in self.add_to_orion_folder.glob("*"):
            if item.is_file():
                print(f"Processing existing file: {item}")
                new, keywords = self.handleFile(str(item))
                self.updateFile(item, new, keywords)

        # Set up watchdog observer for the "Add to Orion" folder
        event_handler = self.OrionEventHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.add_to_orion_folder), recursive=True)
        observer.start()
        print(f"Started monitoring {self.add_to_orion_folder}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Observer stopped.")
        observer.join()

    def updateFile(self, old, new, keywords):
        path = os.path.join(self.orion_folder, new)
        os.rename(old, path)
        self.metadata.appendCSV(path, keywords)
