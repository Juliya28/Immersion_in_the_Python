import argparse
from collections import namedtuple
import logging

from pathlib import Path

"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""


def path_parser(path: str) -> namedtuple:
    DirectoryPath = namedtuple('DirectoryPath', ['name', 'extension', 'drive', 'parent'])

    dir_path = Path(path)
    name = dir_path.stem
    extension = dir_path.suffix
    drive = dir_path.drive
    parent = dir_path.parent

    _path = DirectoryPath(name=name, extension=extension, drive=drive, parent=parent)

    return _path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер пути до директории из командной строки')
    parser.add_argument('path', type=str, help='Путь до директории')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, filename='paths.log', encoding='utf-8')
    logger = logging.getLogger(__name__)
    logger.info(f'args: {args.path} -> result: {path_parser(args.path)}')

    print(path_parser(args.path))