from datetime import datetime

from Note import Note
from Uniq_id import Uniq_id
from Operation import Operation
from Correct_body import Correct_body
from Search_title import Search_title
from Delete_note import Delete_note

def distribute(n):

    file_name = "note.json"

    if n == '1':
        # Создаем заметку
        note = Note(file_name)
        # Устанавливаем идентификатор
        id = Uniq_id(file_name).uniq_id()
        note.set_id(id)
        title = input('Текст заголовка: ')
        note.set_title(title)
        body = input('Текст заметки: ')
        note.set_body(body)
        # время создания заметки
        note.set_created_at(datetime.now())
        # Сохраняем заметку в формате JSON
        note_json = note.to_dict()

        operation = Operation(file_name)
        operation.read_to_write_json(note_json)

    elif n == '2':
        # Печатаем заметку из формата JSON
        Note(file_name).print_note()

    elif n == '3':
        Note(file_name).print_title()
        search = input('Введите имя заголовка для поиска: ')
        new_body = input('Напиши новый текст: ').strip()
        Correct_body(file_name).correct_body(search, new_body, datetime.now())

    elif n == '4':
        Note(file_name).print_title()
        user_search = input('Введите имя заголовка для поиска: ')
        Search_title(file_name).find_body(user_search)

    elif n == '5':
        Note(file_name).print_title()
        delete_note = input('Введите имя заголовка для удаления: ')
        Delete_note(file_name).delete_body(delete_note)
