"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра.
"""

import csv
import json
import os
import pickle
from pathlib import Path

class DataSerializer:
    _HEADERS = ('file', 'parent', 'is_file', 'is_directory', 'size')

    def __init__(self, directory: Path, file=None):
        self.directory = directory
        self.file = file

    def file_revision(self):
        data = {}

        for obj in self.directory.rglob('*'):
            obj_size = sum((file.stat().st_size for file in obj.rglob('*'))) if obj.is_dir() else obj.stat().st_size

            data[obj.name] = {
                'parent': obj.parent.name,
                'is_file': obj.is_file(),
                'is_directory': obj.is_dir(),
                'size': obj_size,
            }
        self._create_files(data)

    def _create_files(self, data):
        with (open(Path(self.directory, 'json_data.json'), 'w', encoding='utf-8') as json_f,
              open(Path(self.directory, 'csv_data.csv'), 'w', newline='', encoding='utf-8') as csv_f,
              open(Path(self.directory, 'pickle_data.pickle'), 'wb') as pickle_f
              ):
            json.dump(data, json_f, indent=2)
            pickle.dump(data, pickle_f)

            csv_writer = csv.writer(csv_f)
            csv_writer.writerow(self._HEADERS)

            for key, value in data.items():
                line = [key]
                values = [val for val in value.values()]
                line.extend(values)
                csv_writer.writerow(line)

    def json_gen(self):
        result = {}
        unique_id = set()

        if self.file.is_file() and os.path.getsize(self.file) > 0:
            with open(self.file, 'r', encoding='utf-8') as js:
                result = json.load(js)
                unique_id.update(*((value.keys()) for value in result.values()))
        while True:
            name, user_id, lvl = input('Введите данные через пробел: ').split()
            if user_id not in unique_id:
                result.setdefault(int(lvl), {}).update({user_id: name})
                with open(self.file, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2)

    def search_json(self):
        for file in self.directory.glob('*.json'):
            with (
                open(file, 'r', encoding='utf-8') as json_f,
                open(Path(self.directory, file.stem + '.pickle'), 'wb') as pickle_f
            ):
                json_data = json.load(json_f)
                pickle.dump(json_data, pickle_f)


if __name__ == '__main__':
    files = DataSerializer(directory=Path.cwd(), file=Path('test.json'))
    files.json_gen()
    files.search_json()