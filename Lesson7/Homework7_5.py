# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def najdovshe_slovo(lst):
    najdovshe = lst[0]
    for value in lst:
        if len(value) > len(najdovshe):
            najdovshe = value
    print(f'Найдовше слово: {najdovshe}')


najdovshe_slovo(['f', '', 'fjihkgjyfh'])