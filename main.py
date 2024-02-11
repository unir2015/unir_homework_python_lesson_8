# main.py
# FILE_NAME = 'phone_book.txt'
from typing import List
# import pandas as pd
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)
    # with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError as err:
    #     print('файла нет. Сначала введите данные\n')
    # else:
    #     print('else')
    # finally:
    #     print('finally')

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

###################################
def copy_file(file):                                                             #создал функцию для копирования файла в другой файл
    try:                                                                         # без этого фукция срабатовал и создовался новый файл
        with open(file, 'r', encoding='utf-8') as f:                             # открываю в режиме для чтения
            lines = f.readlines()                                                # передаю значения на переменую с файла
            with open('copy_file.txt', 'w', encoding='utf-8') as cpf:            # создается новый файл (каждый раз будет перезаписываться )
                cpf.writelines(lines)                                            # передается значения в новый файл
                print('Весь файл успешно скопирован на файл (copy_file.txt)')
    except FileNotFoundError:                                                   # в случае отсутствия основного файла
        print('файла нет. Сначала введите данные\n')
        return []

def copy_search(file):               #создан функция копирования
    with open('copy_search_file.txt', 'w', encoding='utf-8') as cpf:
        cpf.writelines(file)
        print('ваши данные успешно сохранены в файл (copy_search_file.txt)')



def five(file):              #функия для поиска и копирования одного контакта (реализован для входа в дополнительное меню и есть возможность выйти в основное меню)
    file_name = file                  #полученный файл передает в переменую 'file_name"
    data = read_file(file_name)              #открывает файл для чтения с помошью функции 'read_file()'
    founded_data = search_data(data)                 #в поисковую функцию передается файл и результат записывается в переменую 'founded_data'
    show_data(founded_data)              #выводиться на экран

    flag = True              #открывает дополнительное меню
    while flag:
        print('0 - Назад')
        print('1 - Копировать')
        print('2 - Искать заново')
        answer_copy_search = input('Выберите действие: ')
        if answer_copy_search == '0':#закрывает доп меню
            flag = False
        elif answer_copy_search == '1':#с передает результат поискового запроса на функцию копирования файла
            copy_search(founded_data)
        elif answer_copy_search == '2':#для повторного поиска
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - копировать все данные')
        print('5 - найти и копировать определенные данные')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            # data = read_file(file_name)  #присваиваю значение всей папки на переременную 'data'
            # copy_file(data)              #применяю функцию копирования файла
            copy_file(file_name)           # сделал все в одном функции так как при отдельном присваивании функцияя все равно сработал

        elif answer == '5':
            five(file_name)               #Оброшение функции



if __name__ == '__main__':
    main()