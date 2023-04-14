import argparse
import logging
from random import randint

__all__ = [
    'Matrix',
]

"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать, 
○ сравнения, 
○ сложения, 
○ *умножения матриц
"""


_line_size = 3


class Matrix:
    """Создает объект Матрица из заданного списка"""
    _MIN = 0
    _MAX = 100
    _shift = 5
    _FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
    logging.basicConfig(level=logging.INFO, filename='c:/Users/mVm/OneDrive/Рабочий стол/ОБУЧЕНИЕ/Погружение в Python/Immersion_in_the_Python/Lesson_15/matrix.log', 
                        encoding='utf-8', format=_FORMAT, style='{')
    logger = logging.getLogger(__name__)

    def __init__(self, line_size: int = 0, column_size: int = 0, matrix=None):
        if not line_size and not column_size and not matrix:
            self.logger.error('Не введены обязательные данные')
            raise ValueError('Не введены обязательные данные')

        if all((line_size, column_size)):
            self.matrix = [[randint(self._MIN, self._MAX)for _ in range(column_size)] for _ in range(line_size)]
        else:
            self.matrix = matrix
        self._line_size = line_size or len(self.matrix)
        self._column_size = column_size or len(self.matrix[0])

        self.logger.info(f'Объект {self.matrix} создан')

    def __eq__(self, other):
        if self._line_size != other.get_size()[0] or self._column_size != other.get_size()[1]:
            self.logger.info(f'{self=} != {other=}')
            return False

        for i in range(self._line_size):
            for j in range(self._column_size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    self.logger.info(f'{self=} != {other=}')
                    return False
        self.logger.info(f'{self=} = {other=}')
        return True

    def __add__(self, other):
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self._column_size)]
                      for i in range(self._line_size)]
        result = Matrix(matrix=new_matrix)
        self.logger.info(f'{self=} + {other=} = {result=}')
        return result

    def __mul__(self, other):
        result = []
        for i in range(self._line_size):
            spam = []
            for j in range(self._column_size):
                eggs = []
                for k in range(self._line_size):
                    eggs.append(self.matrix[i][k] * other.matrix[k][j])
                spam.append(sum(eggs))
            result.append(spam)

        result = Matrix(matrix=result)
        self.logger.info(f'{self=} * {other=} = {result=}')
        return result

    def __str__(self):
        result = [' '.join(f'{num:>{self._shift}}' for num in line) for line in self.matrix]
        return '\n'.join(result)

    def __repr__(self):
        return f'Matrix({self.matrix})'

    def get_size(self):
        self.logger.info(f'Запрос размерности: {self._line_size}, {self._column_size}')
        return self._line_size, self._column_size


if __name__ == '__main__':
    m1 = Matrix(line_size=2, column_size=3)
    m2 = Matrix(matrix=[[1, 2, 3], [4, 5, 6]])
    print(m1 == m2)
    print(m1 + m2)
    print(m1 * m2)
    err_m = Matrix()

    parser = argparse.ArgumentParser(description='Создание объекта Матрица')
    parser.add_argument('line_size', type=int, help='Количество строк в матрице')
    parser.add_argument('column_size', type=int, help='Количество столбцов в матрице')
    args = parser.parse_args()
    print(Matrix(args.line_size, args.column_size))