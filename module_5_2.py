'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №5.2
Домашняя работа по уроку "Специальные методы классов"
'''


# Задание класса
class House:
    # Задание конструктора класса
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors

   # Задание метода "Вызов лифта" класса
    def go_to(self, new_floor:int):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    # Задание магического метода "Количество этажей" класса
    def __len__(self):
        return self.number_of_floors

    # Задание магического метода "Свойства в строке" класса
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {str(self.number_of_floors)}'


# Создание объектов класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


# Вызов методов класса
print(h1)
print(h2)

print(len(h1))
print(len(h2))
