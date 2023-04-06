from datetime import datetime

import new_notes
import read_json
import write_json


def distribute(n):

    file_name = "note.json"

    if n == '1':
        # Создаем заметку
        note = new_notes.Note("Заголовок заметки", "Текст заметки")
        # Устанавливаем идентификатор
        note.set_id(1)
        # время создания заметки
        note.set_created_at(datetime.now())
        # Сохраняем заметку в формате JSON
        note_json = note.to_dict()
        write_json.write_json(note_json, file_name)
        enter = input('Нажмите Enter для завершения')

    elif n == '2':
        # Восстанавливаем заметку из формата JSON
        restored_note = read_json.read_json(file_name)
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
