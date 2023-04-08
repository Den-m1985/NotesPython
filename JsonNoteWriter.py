import json


class JsonNoteWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, notes):
        with open(self.file_path, "w", encoding='utf-8') as f:
            json.dump(notes, f, indent=4, ensure_ascii=False)
