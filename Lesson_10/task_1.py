"""
Доработаем задачи 5. Создайте класс-фабрику. Класс принимает тип животного 
(название одного из созданных классов) и параметры для этого типа. 
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from Lesson_10 import task_5 as animals

__all__ = [
    'AnimalFactory',
]

class AnimalFactory:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def create_animal(self, *args):
        return self.animal_type(*args)


if __name__ == '__main__':
    dog_factory = AnimalFactory(animals.Dog)
    fish_factory = AnimalFactory(animals.Fish)
    bird_factory = AnimalFactory(animals.Bird)

    print(dog_factory.create_animal(10, 'Richard', 3))
    print(fish_factory.create_animal('red', 'Dory', 1))
    print(bird_factory.create_animal(True, 'Rio', 2))