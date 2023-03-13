"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

def path_maker(path: str) -> tuple:
    *file_path, file_name = path.split('\\')
    file_name, file_extension = file_name.split('.')
    file_path = '\\'.join(file_path)

    return file_path, file_name, file_extension


file_path = 'C:\GB\python_advanced\\task_2.py'
print(path_maker(file_path))