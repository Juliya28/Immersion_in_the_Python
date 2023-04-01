__all__ = [
    'Animal',
]

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return self.color

    def __str__(self):
        return f'Перед нами рыбка по имени {self.name}. Ей {self.age} лет. Её цвет {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, *args):
        self.is_flies = is_flies
        super().__init__(*args)

    def get_params(self):
        param = 'Летает' if self.is_flies else 'Ходит'
        return f'Птичка {self.name} - {param}'

    def __str__(self):
        spam = 'летает' if self.is_flies else 'ходит'
        return f'Перед нами птица по имени {self.name}. Ей {self.age} лет. Эта птица {spam}'


class Dog(Animal):
    SMALL = 10
    BIG = 40

    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height <= self.SMALL:
            return f'Мелкая'
        if self.SMALL < self.height <= self.BIG:
            return 'Норм'
        return 'Большая'

    def __str__(self):
        return f'Перед нами собака по имени {self.name}. Ей {self.age} лет. Её рост {self.height}'


if __name__ == '__main__':
    d = Dog(50, 'Шарик', 5)
    print(d.get_height())