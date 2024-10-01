"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №5.4
Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
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
    # задание переменных класса
    houses_history = []

    # Cоздание и возврат нового экземпляра класса
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    # Задание конструктора класса
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors

    # Задание метода удаления объекта
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        del self

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

# Создание объектов класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del(h2)
del h3

print(House.houses_history)