# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.

#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

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

print(suma_parnyh_chisel(range(10)))

