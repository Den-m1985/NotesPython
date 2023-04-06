import controller

def menu():
    attempts = 0
    while attempts < 3:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # Работает
        print('3. Редактировать заметку')  # надо добавить копирование в json
        print('4. Поиск записи')  # работает
        print('5. Удалить заметку')  # надо сделать
        print('6. Выход\n')  # работает
        number = input('Выберите пункт меню: ')

        if ('0' < number < '6'):
            print('fzbd')
            controller.distribute(number)
        elif (number == '6'):
            break
        else:
            print('Неправильно')
            attempts += 1
