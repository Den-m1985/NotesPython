
def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # Работает
        print('3. Редактировать заметку')  # надо добавить копирование в json
        print('4. Поиск записи')  # работает
        print('5. Удалить заметку')  # надо сделать
        print('6. Выход\n')  # работает
        number = input('Выберите пункт меню: ')
        # controller.distribute(number)
        if number == '6':
            break
