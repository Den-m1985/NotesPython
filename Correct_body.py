from JsonNoteReader import JsonNoteReader
from JsonNoteWriter import JsonNoteWriter


class Correct_body:

    def __init__(self, file_name):
        self.file_name = file_name

    def correct_body(self, title, new_body, datetime):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()

        for item in data:
            if item["title"] == title:
                item["body"] = new_body
                item["created_at"] = datetime.strftime("%Y-%m-%d %H:%M:%S")

        writer = JsonNoteWriter(self.file_name)
        writer.write(data)
