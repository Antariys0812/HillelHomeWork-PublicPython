#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, name, surname, age, serednij_bal = 0):
        self.name = name
        self.surname = surname
        self.age = age
        self.__serednij_bal = serednij_bal

    def get_serednij_bal(self):
        return self.__serednij_bal

    def set_serednij_bal(self, bal):
            self.__serednij_bal = bal

student1 = Student('Olena', 'Gulak', 19)

student1.set_serednij_bal(6)

print(student1.name, student1.surname, student1.age, student1.get_serednij_bal())