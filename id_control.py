import read_json
import Note

'''
def read_notes(cls, filename):
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
'''


def check_id(filename):
    note_dict = new_notes.Note.to_dict()
    id = new_notes.Note.get_id()
    notes = read_json.read_json2(filename)
    if id is None:
        if notes:
            id = max(notes, key=lambda note: note.id).id + 1
        else:
            id = 1
    notes.append()
    notes_dict = [note_dict for note in notes]


@classmethod
def read_max_id(cls, filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            max_id = int(f.read())
    except FileNotFoundError:
        max_id = 0
    return max_id
