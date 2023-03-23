"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит 
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию. 
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с 
учётом всех вложенных файлов и директорий.
"""

import csv
import json
from pathlib import Path
import pickle
import os

__all__ = [
    'recursion',
]


def recursion(directory: Path):
    data = {}
    headers = ('file', 'parent', 'is_file', 'is_directory', 'size')

    for obj in directory.rglob('*'):
        obj_size = sum((file.stat().st_size for file in obj.rglob('*'))) if obj.is_dir() else obj.stat().st_size

        data[obj.name] = {
            'parent': obj.parent.name,
            'is_file': obj.is_file(),
            'is_directory': obj.is_dir(),
            'size': obj_size,
        }

    with (open(Path(directory, 'json_data.json'), 'w', encoding='utf-8') as json_f,
          open(Path(directory, 'csv_data.csv'), 'w', newline='', encoding='utf-8') as csv_f,
          open(Path(directory, 'pickle_data.pickle'), 'wb') as pickle_f
          ):
        json.dump(data, json_f, indent=2)
        pickle.dump(data, pickle_f)

        csv_writer = csv.writer(csv_f)
        csv_writer.writerow(headers)

        for key, value in data.items():
            line = [key]
            values = [val for val in value.values()]
            line.extend(values)
            csv_writer.writerow(line)


if __name__ == '__main__':
    recursion(Path('files'))