"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №6.1
Домашнее задание по теме "Зачем нужно наследование"
"""

# Животные
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    # Метод поедания животным растения
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


# Растения
class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

# Млекопитающие
class Mammal(Animal):
    pass

# Хищники
class Predator(Animal):
    pass

# Цветы
class Flower(Plant):
    pass

# Фрукты
class Fruit(Plant):
    edible = True


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