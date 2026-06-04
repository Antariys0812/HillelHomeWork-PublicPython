
# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.

# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

def kilkist_unic_symvoliv(ryadok: str):
    '''
    :param ryadok: string
    :return: True if there are more then 10 symbols in string, else - False
    '''
    if len(set(ryadok)) > 10:
        return True
    else:
        return False

print(kilkist_unic_symvoliv(input('Введи рядок: ')))