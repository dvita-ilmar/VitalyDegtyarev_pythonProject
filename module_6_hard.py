"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №6.hard
Дополнительное практическое задание по модулю: "Наследование классов."
"""

from math import pi, sqrt

class Figure:
    SIDES_COUNT = 0 # Количество сторон

    # Конструктор фигуры
    def __init__(self, color, *sides:int):
        self.__color = list(color)
        self.__sides = []
        # Странная, но соответствующая ТЗ в разделе "ВАЖНО!" проверка на количество переданных сторон
        if len(sides) != self.SIDES_COUNT:
            if len(sides) == 1:
                size = sides[0]
            else:
                size = 1
            for i in range(1, self.SIDES_COUNT + 1):
                self.__sides.append(size)
        else:
            self.__sides = list(sides)
        self.filled = False

    # Возвращает цвета фигуры
    def get_color(self):
        return self.__color

    # Проверяет переданные значения цвета на корректность (служебная)
    def __is_valid_color(self, r:int, g:int, b:int):
        if r in range(0, 256) and g in range(0, 256) and b in range(0,256):
            return True
        else:
            return False

    # Устанавливает новые цвета фигуры
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    #  Проверяет переданные значения сторон на корректность (служебная)
    def  __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.SIDES_COUNT:
            return False
        result_check = True
        for new_side in new_sides:
            if not isinstance(new_side, int) or new_side <= 0:
                result_check = False
                break
        return result_check

    # Возвращает стороны фигуры
    def get_sides(self):
        return self.__sides

    # Возвращает периметр фигуры
    def __len__(self):
        return sum(self.__sides)

    # Устанавливает новые стороны фигуры
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):

    SIDES_COUNT = 1 # Количество сторон круга

    # Переопределение конструктора из-за необходимости рассчитать еще и радиус
    def __init__(self, color, *sides:int):
        super().__init__(color, *sides)
        self.__radius = len(self) / (2 * pi)

    # Переопределение на свою "установку сторон" из-за необходимости автоматически перерассчитывать новый радиус
    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = len(self) / (2 * pi)

    # Возвращает площадь круга
    def get_square(self):
        return pi * self.__radius ** 2

    # Возвращает радиус круга
    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    SIDES_COUNT = 3 # Количество сторон треугольника

    # Возвращает площадь треугольника
    def get_square(self):
        p = len(self) / 2
        print(p)
        a, b, c = self.get_sides()
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    SIDES_COUNT = 12 # Количество сторон куба

    # Переопределение конструктора из-за необходимости "переопределить" параметр __sides
    def __init__(self, color, *sides:int):
        super().__init__(color, *sides)

        # Закрытый атрибут не переопределяется вне своего класса определения! - оставляю по условию ТЗ
        # (при выходе из данного класса атрибуту __sides объекта класса куб возвращается значение от класса figure)
        self.__sides = [sides[0], sides[0], sides[0], sides[0], sides[0], sides[0], sides[0], sides[0], sides[0],
                            sides[0], sides[0], sides[0],]
        print(f'Внутри класса Cube: {self.__sides}') # Служебная печать - чтобы показать разницу

    # Возвращает объем куба
    def get_volume(self):
        return self.get_sides()[0] ** 3

# Запуск
if __name__ == '__main__':

    circle1 = Circle((200, 200, 100), 100)
    print(f'НАЧАЛО: {circle1.get_sides()}')
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    circle1.set_sides(15) # Изменится
    print(f'Стороны круга: {circle1.get_sides()}')
    print(f'Длина окружности: {len(circle1)}')
    print(f'Радиус круга: {circle1.get_radius()}')
    print(f'Площадь круга: {circle1.get_square()}')

    # Проверка единственного публичного атрибута filled на доступность напрямую
    print(f'Круг закрашен: {circle1.filled}')
    circle1.filled = True
    print(f'Круг закрашен: {circle1.filled}')
    
    triangle1 = Triangle((100, 100, 100), 10, 20, 20)
    print(f'Стороны треугольника: {triangle1.get_sides()}')
    print(f'Площадь треугольника: {triangle1.get_square()}')

    cub0 = Cube((250, 230, 210), 30, 4, 6)
    print(cub0.get_color(), cub0.get_sides(), 'В итоге сохраняется атрибут __sides от класса Figure')
    print(f'Объем куба: {cub0.get_volume()}')

    cub = Cube((255, 255, 255), 30)
    print(cub.get_color(), cub.get_sides(), 'И здесь сохраняется атрибут __sides от класса Figure-считаю это правильно')
    print(f'Объем куба: {cub.get_volume()}')

    cube1 = Cube((1, 1, 1), 12, 15, 17, 23, 45, 13, 47, 2, 4, 5, 7, 12)
    print(cube1.get_color(), cube1.get_sides(), 'Но стороны куба не изменились!')

    cube1.set_color(10,255,0)
    cube1.set_sides(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    print(cube1.get_color(), cube1.get_sides(), 'Периметр: ',len(cube1))
    print(f'Объем куба: {cube1.get_volume()}')