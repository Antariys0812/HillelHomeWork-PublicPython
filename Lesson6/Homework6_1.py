# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

pryklad = input('Введи рядок: ')

# Спосіб 1
print(bool(len(set(pryklad)) > 10))
# Спосіб 2
if len(set(pryklad)) > 10:
    print(True)
else:
    print(False)

