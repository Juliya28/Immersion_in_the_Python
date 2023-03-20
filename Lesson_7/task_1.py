# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔ Каждая группа включает файлы с несколькими расширениями. 
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import mimetypes
from pathlib import Path

__all__ = [
    'file_sorter',
]


FILE_TYPES = ('video', 'image', 'text')


def file_sorter(directory: Path):
    for file_type in FILE_TYPES:
        Path(directory, file_type).mkdir(parents=True, exist_ok=True)

    for file in directory.iterdir():
        _file_type, _ = mimetypes.guess_type(file)
        file_type = _file_type.split('/')[0] if _file_type else None

        if file_type and file_type in FILE_TYPES:
            file.replace(file.parent / file_type / file.name)


if __name__ == '__main__':
    file_sorter(Path('files'))