import controller

def menu():
    attempts = 0
    while attempts < 3:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')
        print('2. Вывод записей на экран')
        print('3. Редактировать заметку')
        print('4. Поиск записи')
        print('5. Удалить заметку')
        print('6. Выход\n')
        number = input('Выберите пункт меню: ')

        if ('0' < number < '6'):
            controller.distribute(number)
        elif (number == '6'):
            break
        else:
            print('Неправильно')
            attempts += 1
