"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №6.2
Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
"""


# Описание класса автотранспорт
class Vehicle:
    __COLOR_VARIANTS = ['white', 'gray', 'black', 'red', 'green', 'brown', 'blue', 'metallic']  # Доступные цвета авто


    def __init__(self, owner:str, model:str, engine_power:int, color:str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    # Возвращает название модели транспорта
    def get_model(self):
        print(f'Модель: {self.__model}')


    # Возвращает мощность двигателя
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')


    # Возвращает цвет транспорта
    def get_color(self):
        print(f'Цвет: {self.__color}')


    # Выдает полное инфо о транспорте
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()


    # меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS
    def set_color(self, new_color:str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


# Описание класса седан
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # Ограничение по классу седан на 5 пассажиров


# Запуск
if __name__ == '__main__':
    vehicle1 = Sedan('Иванов', 'Седан LADA Granta', 90, 'metallic')

    # Изначальные свойства
    vehicle1.print_info() # Модель: Седан LADA Granta Мощность двигателя: 90 Цвет: metallic

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink') # Нельзя сменить цвет на Pink
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Петров'

    # Проверяем что поменялось
    vehicle1.print_info() # Модель: Седан LADA Granta Мощность двигателя: 90 Цвет: BLACK

    # Проверка запрещенных операций
    #Vehicle.__COLOR_VARIANTS.append('pink') #- AttributeError: type object 'Vehicle' has no attribute '__COLOR_VARIANTS'
    #print(Vehicle.__COLOR_VARIANTS) # AttributeError: type object 'Vehicle' has no attribute '__COLOR_VARIANTS'
    # Атрибут класса __COLOR_VARIANTS не виден совсем - это должно быть правильно

    Sedan.__PASSENGERS_LIMIT = 6
    print(Sedan.__PASSENGERS_LIMIT) # 6
    # Атрибут __PASSENGERS_LIMIT и виден и доступен для изменения - и это странно!?

    vehicle1.__model = 'Лошадь с телегой'
    vehicle1.__engine_power = '500'
    vehicle1.__color = 'LETTUCE'
    vehicle1.print_info() # Модель: Седан LADA Granta Мощность двигателя: 90 Цвет: BLACK - ничего не изменилось - это правильно

    # Не все сокрытия в классах почему-то работают правильно!!!
