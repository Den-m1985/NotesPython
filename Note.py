import json


class Note:
    def __init__(self, title, body):
        self.id = None  # идентификатор
        self.title = title  # заголовок
        self.body = body  # тело заметки
        self.created_at = None  # дату/время создания

    def set_id(self, note_id):
        self.id = note_id

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def to_dict(self):
        note_dict = {}
        note_dict["id"] = self.id
        note_dict["title"] = self.title
        note_dict["body"] = self.body
        note_dict["created_at"] = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return note_dict

    def print_note(self):
        print(self.title)
        print(self.body)
        print(self.created_at)


    @classmethod
    def from_dict(cls, note_dict):
        return cls(
            note_dict["title"],
            note_dict["body"],
            note_dict["created_at"]
        )

    @classmethod
    def read_notes(cls, filename):
        notes = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                notes_dict = json.load(f)
                for note_dict in notes_dict:
                    note = cls.from_dict(note_dict)
                    notes.append(note)
        except FileNotFoundError:
            pass
        return notes

    @classmethod
    def read_max_id(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                max_id = int(f.read())
        except FileNotFoundError:
            max_id = 0
        return max_id

    @classmethod
    def write_max_id(cls, filename, max_id):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(max_id))

    @classmethod
    def generate_id(cls, filename):
        max_id = cls.read_max_id(filename) + 1
        cls.write_max_id(filename, max_id)
        return max_id
