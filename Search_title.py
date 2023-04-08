from JsonNoteReader import JsonNoteReader


class Search_title:

    def __init__(self, file_name):
        self.file_name = file_name

    def find_body(self, title):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()

        for item in data:
            if item["title"] == title:
                print(item["body"])
