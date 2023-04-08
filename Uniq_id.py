from JsonNoteReader import JsonNoteReader


class Uniq_id:

    def __init__(self, file_name):
        self.file_name = file_name

    def uniq_id(self):
        number = self.find_id()
        id = number + 1
        return id

    def find_id(self):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()

        max_id = 0
        for item in data:
            if item["id"] > max_id:
                max_id = item["id"]
        return max_id
