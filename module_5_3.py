"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №5.3
Домашняя работа по уроку "Перегрузка операторов."
"""

# Функция проверяет типы данных и сравнивает операнды по также переданному логическому оператору
def oper_gen(self, other, op): # op - передаваемый в функцию символ(ы) логического оператора сравнения
    if isinstance(other, int):
        if eval(str(self.number_of_floors) + op + str(other)):
            return True
        else:
            return False
    elif isinstance(other, House):
        if eval(str(self.number_of_floors) + op + str(other.number_of_floors)):
            return True
        else:
            return False
    else:
        print('Error: Invalid data type')
        return None


# Задание класса House
class House:
    # Задание конструктора класса
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors

   # Задание метода "Вызов лифта" класса
    def go_to(self, new_floor:int):
        if new_floor > self.number_of_floors:
            print('Error: Elevator out of range')
        else:
            for i in range(1, new_floor+1):
                print(i)

    # Задание специального "магического" метода "Количество этажей" класса
    def __len__(self):
        return self.number_of_floors

    # Задание специального "магического" метода "Свойства в строке" класса
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {str(self.number_of_floors)}'

    # Перегрузка оператора '=='
    def __eq__(self, other):
        op = '=='
        return oper_gen(self, other, op)

    # Перегрузка оператора '<'
    def __lt__(self, other):
        op = '<'
        return oper_gen(self, other, op)

    # Перегрузка оператора '<='
    def __le__(self, other):
        op = '<='
        return oper_gen(self, other, op)

    # Перегрузка оператора '>'
    def __gt__(self, other):
        op = '>'
        return oper_gen(self, other, op)

    # Перегрузка оператора '>='
    def __ge__(self, other):
        op = '>='
        return oper_gen(self, other, op)

    # Перегрузка оператора '!='
    def __ne__(self, other):
        op = '!='
        return oper_gen(self, other, op)

    # Перегрузка оператора 'self + other'
    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        else:
            print('Error: Invalid data type')
            return self

    # Перегрузка оператора 'other + self'
    def __radd__(self, other):
        return self.__add__(other)

    # Перегрузка оператора 'self += other'
    def __iadd__(self, other):
        return self.__add__(other)

# Задание другого класса для примера неверного типа данных
class Mouse:
    # Задание конструктора класса
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors


# Создание объектов класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = Mouse('Мышь белая', 1)

# Вызовы
print(h1) # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2) # Название: ЖК Акация, кол-во этажей: 20
print(h3) # <__main__.Mouse object at 0x000002743118F0B0> (т.к. магический метод __str__ в этом классе не задан)

# С ошибкой типа
print(h1 == h3) # None Error: Invalid data type
print(h1 < 10.5) # None Error: Invalid data type

# Логические
print(h1 == h2) # __eq__ (False)
print(h1 > h2) # __gt__ (False)
print(h1 >= h2) # __ge__ (False)
print(h1 < h2) # __lt__ (True)
print(h1 <= h2) # __le__ (True)
print(h1 != h2) # __ne__ (True)

# Арифметические
h1 = h1 + 10 # __add__
print(h1) # Название: ЖК Эльбрус, кол-во этажей: 20

h1 = h1 + h2 # __add__
print(h1) # Название: ЖК Эльбрус, кол-во этажей: 40

h2 = 10 + h2 # __radd__
print(h2) # Название: ЖК Акация, кол-во этажей: 30

h2 += 10 # __iadd__
print(h2) # Название: ЖК Акация, кол-во этажей: 40

h2 += h1 # object += object
print(h2) # Название: ЖК Акация, кол-во этажей: 80

h1 = h1 + '10' # Error: Invalid data type
print(h1) # Название: ЖК Эльбрус, кол-во этажей: 40 (не изменилось)

h2 += h3 # Error: Invalid data type
print(h2) # Название: ЖК Акация, кол-во этажей: 80 (не изменилось)