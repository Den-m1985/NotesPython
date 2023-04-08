from JsonNoteReader import JsonNoteReader
from JsonNoteWriter import JsonNoteWriter


class Delete_note:

    def __init__(self, file_name):
        self.file_name = file_name

    def delete_body(self, title):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()

        new_data = []
        for item in data:
            if item["title"] != title:
                new_data.append(item)

        writer = JsonNoteWriter(self.file_name)
        writer.write(new_data)
