import json
import datetime
import Note


def read_json(filename):
    notes = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes_dict = json.load(f)
            for note_dict in notes_dict:
                note = new_notes.Note.from_dict(note_dict)
                notes.append(note)
    except FileNotFoundError:
        pass
    return notes


def read_json2(filename):
    data = []
    with open(filename, "r", encoding='utf-8') as f:
        notes_dict = json.load(f)
        for i in notes_dict:
            print(i)
            #g = list(i)
            data.append(i)
    return data


@classmethod
def from_json(cls, note_json):
    note_dict = json.loads(note_json)
    return cls.from_dict(note_dict)


@classmethod
def load_from_file(cls, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        note_dict = json.load(f)
    return cls.from_dict(note_dict)


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


'''
       Если sure_ascii имеет значение true (по умолчанию), 
       в выводе гарантированно будут экранированы все входящие символы, отличные от ASCII. 
       Если sure_ascii имеет значение false, эти символы будут выводиться как есть.  
'''
