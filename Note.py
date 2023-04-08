from JsonNoteReader import JsonNoteReader


class Note:
    def __init__(self, file_name):
        self.id = None  # идентификатор
        self.created_at = None  # дату/время создания
        self.file_name = file_name

    def set_id(self, note_id):
        self.id = note_id

    # заголовок
    def set_title(self, title):
        self.title = title

    # тело заметки
    def set_body(self, body):
        self.body = body

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created_at

    def to_dict(self):
        note_dict = {}
        note_dict["id"] = self.id
        note_dict["title"] = self.title
        note_dict["body"] = self.body
        note_dict["created_at"] = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return note_dict

    def print_note(self):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()
        sorted_data = sorted(data, key=lambda item: item['created_at'])
        for item in sorted_data:
            print(f'--{item["title"]}--')
            print(item["body"])
            print(item["created_at"])
            print()

    def print_title(self):
        reader = JsonNoteReader(self.file_name)
        data = reader.read()
        print('Список заголовков:')
        for item in data:
            print(f'--{item["title"]}--')