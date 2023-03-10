"""Напишите функцию для транспонирования матрицы
"""

def matrix_transponition(matrix: list[list]) -> list[list]:
    matrix_2 = []

    for i in range(len(matrix[0])):
        list1 = []
        for j in range(len(matrix)):
            list1.append(matrix[j][i])
        matrix_2.append(list1)

    return matrix_2


matrix = [[1, 3, 5], [2, 4, 6], [7, 9, 11], [8, 10, 12]]
print(f'Транспонированная матрица: {matrix_transponition(matrix)}\n')
