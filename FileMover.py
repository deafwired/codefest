import os
import shutil

class FileMover:
    def __init__(self, destination_path: str, new_file_name: str):
        self.destination_path = destination_path
        self.new_file_name = new_file_name

    def move_file(self, source_file: str):
        if not os.path.isfile(source_file):
            raise FileNotFoundError(f"Source file '{source_file}' does not exist.")

        if not os.path.exists(self.destination_path):
            os.makedirs(self.destination_path)

        destination_file = os.path.join(self.destination_path, self.new_file_name)
        shutil.move(source_file, destination_file)

        return destination_file