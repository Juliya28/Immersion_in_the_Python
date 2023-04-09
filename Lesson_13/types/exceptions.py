__all__ = [
    'NotInteger',
    'NotString',
]


class BaseTypeException(Exception):
    pass


class NotInteger(BaseTypeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Вы ввели не целое число, а {type(self.value)}'


class NotString(BaseTypeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Вы ввели не строку/текст, а {type(self.value)}'