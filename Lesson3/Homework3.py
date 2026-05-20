import math
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

#Перший спосіб
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal '
                       'on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it '
                       'doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an '
                       'explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)

#Другий спосіб
alice_in_wonderland1 = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where ——" said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'''
print(alice_in_wonderland1)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
chorne_more = 436_402
azovske_more = 37_800
zahalna_plosha = chorne_more + azovske_more
print(f'Загальна площа - {zahalna_plosha}')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

suma_tovariv: int = 375_291
first_and_second_floors: int = 250_449
second_and_third_floors: int = 222_950
third_floor: int = suma_tovariv - first_and_second_floors
second_floor: int = second_and_third_floors - third_floor
first_floor: int = first_and_second_floors - second_floor
print(f'Перший поверх - {first_floor}\nДругий поверх - {second_floor}\nТретій поверх - {third_floor}')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

months = 18
price = 1179
total_price= price * months
print(f'Вартість комп’ютера - {total_price}')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print(f'Остача: a) {8019%8} b) {9907%9} c) {2789%5} d) {7248%6} e) {7128%5} f) {19224%9}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

#Перший спосіб
piza_velyka = 274
piza_serednya = 218
sik = 35
tort = 350
voda = 21
suma_groshej = piza_velyka*4 + piza_serednya*2 + sik*4 + tort*1 + voda*3
print(f'Сума грошей на день народження - {suma_groshej}')

#Другий спосіб
tovary ={"piza_velyka": 274, "piza_serednya": 218, "sik": 35, "tort": 350, "voda": 21}
print(f'Сума грошей на день народження - {tovary["piza_velyka"]*4 + tovary["piza_serednya"]*2 + tovary["sik"]*4 + tovary["tort"] + tovary["voda"]*3}')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

kilkist_foto = 232
storinka_capacity = 8
kilkist_storinok = kilkist_foto // storinka_capacity
if (kilkist_foto % storinka_capacity) > 0 :
    kilkist_storinok += 1
print(f'Кількість сторінок - {kilkist_storinok}')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

vidstan = 1600
benzin_na_100km = 9
mistkist_baku = 48
buk_na_pochatku = 0
kilkist_benzinu = vidstan/100*benzin_na_100km - buk_na_pochatku
kilkist_zapravok = math.ceil(kilkist_benzinu / mistkist_baku)
print(f'Кількість бензину - {kilkist_benzinu}, Кількість заправок - {int(kilkist_zapravok)}')

