"""
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. 
    При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла. 
    Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона 
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

from pathlib import Path

__all__ = [
    'group_name',
]


def group_name(directory: Path, qty_num: int, old_ext: str, new_ext: str, sym_range: list[int], new_name: str = ''):
    for i, file in enumerate(directory.glob(f'*.{old_ext}'), start=1):
        file_name_, _ = file.name.split('.')
        start = min(sym_range[0], len(file_name_))
        stop = min(sym_range[1], len(file_name_))
        file_name = file_name_[start:stop]
        new_file_name = f'{file_name}{new_name}{i:0{qty_num}}.{new_ext}'

        file.rename(file.parent / new_file_name)


if __name__ == '__main__':
    group_name(Path('files'), qty_num=3, old_ext='bin', new_ext='txt', sym_range=[2, 6], new_name='_test_')