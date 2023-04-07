import json


class JsonNoteReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            # Если файла нет — создаём новый и записываем в него новый объект
            with open(self.file_path, 'w') as file:
                data = []
                json.dump(data, file)
                return data
