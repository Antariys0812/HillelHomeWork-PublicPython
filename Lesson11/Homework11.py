masyv = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def calculate_suma(comma_delimited_string):
    numbers = comma_delimited_string.split(',')
    try:
        suma = 0
        for i in numbers:
            suma += int(i)
        print(suma)
    except ValueError as e:
        print('Не можу це зробити')

for i in masyv:
    calculate_suma(i)
