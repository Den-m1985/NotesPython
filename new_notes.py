import json
import datetime


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

    def set_created_at(self, created_at):
        self.created_at = created_at

    def to_dict(self):
        note_dict = {}
        note_dict["id"] = self.id
        note_dict["title"] = self.title
        note_dict["body"] = self.body
        note_dict["created_at"] = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return note_dict


    @classmethod
    def from_dict(cls, note_dict):
        note = cls(note_dict["title"], note_dict["body"])
        note.set_id(note_dict["id"])
        note.set_created_at(datetime.datetime.strptime(note_dict["created_at"], "%Y-%m-%d %H:%M:%S"))
        return note

    '''
    @classmethod
    def from_json(cls, note_json):
        note_dict = json.loads(note_json)
        return cls.from_dict(note_dict)
'''