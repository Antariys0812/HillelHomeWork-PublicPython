# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def seredne(lst):
    counter = 0
    for number in lst:
        counter = counter + number
    print(f'Cереднє арифметичне: {counter/len(lst)}')

seredne([1, 8, 3])
