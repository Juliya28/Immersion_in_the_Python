import Lesson_13.types.exceptions as types_exceptions


def prime_gen(number: int):
    try:
        int(number)
    except ValueError:
        raise types_exceptions.NotInteger(number)

    start = 2
    stop = number + 1

    for num in range(start, stop):
        limit = num // start + 1

        for div in range(start, limit):
            if not num % div:
                break
        else:
            yield num


def path_maker(path: str) -> tuple:
    if not isinstance(path, str):
        raise types_exceptions.NotString(path)

    *file_path, file_name = path.split('\\')
    file_name, file_extension = file_name.split('.')
    file_path = '\\'.join(file_path)

    return file_path, file_name, file_extension


file_path = 25
# print(path_maker(file_path))

num = 'двадцать пять'
# print(*prime_gen(num))
