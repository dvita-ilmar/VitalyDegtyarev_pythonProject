"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №6.3
Домашнее задание по теме "Множественное наследование"
"""


class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        if isinstance(self, Pegasus): # Если создается объект класса Pegasus то
            super().__init__() # унаследовать ему свойства и от класса Eagle


    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Запуск
if __name__ == '__main__':
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()