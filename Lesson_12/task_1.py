"""
Создайте класс студента. 
✯ Используя дескрипторы проверяйте ФИО на первую заглавную букву и 
наличие только букв. 
✯ Названия предметов должны загружаться из файла CSV при создании 
экземпляра. Другие предметы в экземпляре недопустимы. 
✯ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты 
тестов (от 0 до 100). 
✯ Также экземпляр должен сообщать средний балл по тестам для каждого 
предмета и по оценкам всех предметов вместе взятых. 
"""

import csv
from pathlib import Path


class NameValidate:
    """Проверяет ФИО на первую заглавную букву и наличие только букв."""

    def __init__(self, title_check, char_check):
        self.title_check = title_check
        self.char_check = char_check

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not self.title_check(value) or not self.char_check(value):
            raise ValueError(f'Invalid {self.param_name} of user - {value}')
        setattr(instance, self.param_name, value)


class Student:
    _MIN_GRADE = 2
    _MAX_GRADE = 5
    _MIN_TEST_RATE = 0
    _MAX_TEST_RATE = 100
    _RESULTS = ('grades', 'rates')

    first_name = NameValidate(str.istitle, str.isalpha)
    last_name = NameValidate(str.istitle, str.isalpha)

    def __init__(self, first_name: str, last_name: str, subject_file: Path = Path('subjects.csv')):
        self._first_name = first_name
        self._last_name = last_name
        self.__subjects_results = self._dict_subject_maker(subject_file)

    def __str__(self):
        return f'Студент {self._first_name} {self._last_name}'

    @property
    def results(self):
        grade_size = 0
        results = {'Средний балл по оценкам всех предметов': 0}

        for key, value in self.__subjects_results.items():
            grade = self._RESULTS[0]
            rate = self._RESULTS[1]
            rate_size = len(value[rate])

            if rate_size:
                results[f'Средний бал по тестам для {key}'] = round(sum(value[rate]) / rate_size, 2)
            else:
                results[key] = 0

            results['Средний балл по оценкам всех предметов'] += sum(value[grade])
            grade_size += len(value[grade])

        if grade_size:
            results['Средний балл по оценкам всех предметов'] = \
                round(results['Средний балл по оценкам всех предметов'] / grade_size, 2)

        return results

    @property
    def subjects(self):
        return self.__subjects_results.keys()

    @property
    def all_results(self):
        return self.__subjects_results

    @property
    def full_name(self):
        return self._first_name + self._last_name

    def add_grade(self, subject: str, grade: int):
        value = self._RESULTS[0]
        self._check_values(subject, grade, self._MIN_GRADE, self._MAX_GRADE)
        self.__subjects_results[subject][value].append(grade)
        return f'Оценка успешно добавлена'

    def add_test_rate(self, subject: str, rate: int):
        value = self._RESULTS[1]
        self._check_values(subject, rate, self._MIN_TEST_RATE, self._MAX_TEST_RATE)
        self.__subjects_results[subject][value].append(rate)
        return f'Оценка успешно добавлена'

    def _check_values(self, subject: str, value: int, min_value: int, max_value: int):
        if subject not in self.__subjects_results:
            raise ValueError(f'Предмет {subject} не входит в учебную программу')
        if value > max_value or value < min_value:
            raise ValueError(f'Оценка {value} не входит в требуемый диапазон')

    def _dict_subject_maker(self, subject_file: Path):
        subjects = {}

        with open(subject_file, 'r', encoding='utf-8', newline='') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                subjects[line[0]] = {self._RESULTS[0]: [], self._RESULTS[1]: []}

        return subjects


if __name__ == '__main__':
    s1 = Student('Иван', 'Иванов', Path('subjects.csv'))
    print(s1.add_grade('Математика', 5))
    print(s1.add_grade('Математика', 4))
    print(s1.add_grade('Русский язык', 2))
    print(s1.add_test_rate('Математика', 50))
    print(s1.add_test_rate('Математика', 100))
    print(s1.add_test_rate('Русский язык', 80))
    print(s1.results)
    print(s1.subjects)
    print(s1.all_results)