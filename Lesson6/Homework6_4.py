#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list1 = list(range(10))
print(list1)
counter = 0
for i in list1:
    if i%2 == 0:
        counter = counter + i
print(counter)

