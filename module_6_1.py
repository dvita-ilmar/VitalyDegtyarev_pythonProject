"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №6.1
Домашнее задание по теме "Зачем нужно наследование"
"""

# Животные
class Animal:
    alive = True
    fed = False


# Растения
class Plant:
    edible = False


# Млекопитающие
class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


# Хищники
class Predator(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

# Цветы
class Flower(Plant):
    def __init__(self, name):
        self.name = name

# Фрукты
class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


# Запуск
if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)