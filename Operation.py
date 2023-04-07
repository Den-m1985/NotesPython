from JsonNoteReader import JsonNoteReader
from JsonNoteWriter import JsonNoteWriter


class Operation:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_to_write_json(self, note_json):
        reader = JsonNoteReader(self.file_path)
        data = reader.read()

        if data:
            data.append(note_json)
        else:
            data.append(note_json)

        writer = JsonNoteWriter(self.file_path)
        writer.write(data)
