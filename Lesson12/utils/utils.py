# task 7_2
"""Написати функцію, яка обчислює суму двох чисел."""

def suma(number1, number2):
    return number1 + number2

# task 7_4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""

def string_reverse(arg):
    return arg[::-1]

# task 7_9
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""

def suma_parnyh_chisel(list1):
    '''
    :param list1: list
    :return: int, sum of even numbers
    '''
    suma = 0
    for i in list1:
        if i%2 == 0:
            suma = suma + i
    return suma

# task 6_3
"""
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Дані в лісті можуть бути будь якими
"""

def list_string(lst1):
    lst2 = []
    for i in lst1:
        if type(i) == str:
            lst2.append(i)
    return lst2

# task 3_9
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

def calculate_kilkist_storinok(kilkist_foto, storinka_capacity):
    kilkist_storinok = kilkist_foto // storinka_capacity
    if (kilkist_foto % storinka_capacity) > 0:
        kilkist_storinok += 1
    return kilkist_storinok