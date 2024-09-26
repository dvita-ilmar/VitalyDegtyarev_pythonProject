'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №5.1
Домашняя работа по уроку "Атрибуты и методы объекта."
'''


# Задание класса
class House:
    # Задание конструктора класса
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors

   # Задание метода класса
    def go_to(self, new_floor:int):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)


# Создание объектов класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)


# Вызов методов класса
h1.go_to(5)
h2.go_to(10)