# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def dict_maker(**kwargs) -> dict:
    result = {}

    for key, item in kwargs.items():
        item = str(item) if isinstance(item, (list, set, dict)) else item
        result[item] = key if item not in result else [result.get(item)] + [key]

    return result


print(f'Словарь без повторений, но с изменяемыми типами: {dict_maker(a=1, b=3, c=[1, {2, 3}], d={"a": 5, "b": 7})}\n')
print(f'Словарь с повторениями: {dict_maker(a=1, b=1, c=2, d=3, e=3)}\n')