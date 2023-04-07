from datetime import datetime

import Note
from JsonNoteReader import JsonNoteReader
from Operation import Operation


def distribute(n):

    file_name = "note.json"

    if n == '1':
        # Создаем заметку
        note = Note.Note("Заголовок заметки", "Текст заметки")
        # Устанавливаем идентификатор
        note.set_id(1)
        # время создания заметки
        note.set_created_at(datetime.now())
        # Сохраняем заметку в формате JSON
        note_json = note.to_dict()

        operation = Operation(file_name)
        operation.read_to_write_json(note_json)
        #writer = JsonNoteWriter(file_name)
        #writer.write(note_json)
        #new_notes.Note.write_notes(file_name, note_json)
        #write_json.write_json(note_json, file_name)
        enter = input('Нажмите Enter для завершения')

    elif n == '2':
        # Восстанавливаем заметку из формата JSON
        #reader = JsonNoteReader(file_name)
        #read_notes = reader.read()
        note = Note.Note("Заголовок заметки", "Текст заметки")
        note.print_note()

        enter = input('Нажмите Enter для выхода в меню ')

    elif n == '3':
        #operations.refactor()
        enter = input('Нажмите Enter для выхода в меню ')

    elif n == '4':
        user_search = input('Введите имя для поиска?: ')
        #searchcontact.searchcontact(user_search)
        enter = input('Нажмите Enter для завершения')

    elif n == '5':
        #delete()
        enter = input('Нажмите Enter для завершения')
