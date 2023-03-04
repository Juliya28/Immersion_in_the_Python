# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

text = """Новые и недавно измененные материалы:
Связка Flask + Nginx + Gunicorn + Gevent на VDS.
Разворачиваем связку Flask + nginx + gunicorn + gevent на VDS сервере. 
Материал будет похож на HOWTO с примерами конфигов .
Предварительные требования - это работающее приложение Flask на локальном компьютере, 
сервер VDS с установленной OS Ubuntu или Debian с доступом sudo или root.
Как изменить размеры строки/столбца модулем openpyxl в Python.
В материале рассказывается о методах объектов модуля openpyxl, которые отвечают за такие 
свойства документа XLSX как изменение размеров строки и столбца, а также их сворачивание/скрытие при открытии 
электронной таблицы в программе Excel.
Пример структуры приложения Flask как пакета Python.
Для больших приложений рекомендуется использовать структуру пакет Python вместо модуля. Что мы от этого выиграем? 
Теперь можно реструктурировать приложение на несколько модулей. А в дальнейшем можно безболезненно расширять веб-приложение.
Конструкция match/case в Python, сопоставление с образцом.
В Python 3.10 введена новая конструкция match/case, которая называется *Structural pattern matching*
(соответствие структуре шаблона). Сопоставление списков, словарей, сложных структур и классов.
Методы экземпляра datetime.datetime() в Python.
В этом разделе рассмотрены методы экземпляра класса datetime.datetime с примерами.
Методы экземпляра datetime.date() в Python.
В этом разделе рассмотрены методы экземпляра класса datetime.date с примерами.
Исключения ExceptionGroup и BaseExceptionGroup в Python.
Исключения ExceptionGroup и BaseExceptionGroup заключают исключения в последовательность excs.
Аргумент msg должен быть строкой. Разница между этими двумя классами заключается в том,
что BaseExceptionGroup расширяет BaseException и может обертывать любое исключение, а ExceptionGroup расширяет Excep
Базовые классы исключений в Python.
Следующие исключения используются в основном как базовые классы для других исключений.
Математические и побитовые функции модуля operator в Python.
Арифметические и побитовые операторы для манипулирования числовыми значениями также 
поддерживаются и являются самыми многочисленными."""

FRE_WORDS = 10

words = text.split()
qty_words = {}

for item in words:
    if item.isalpha():
        _word = item.lower()
        qty_words[_word] = qty_words.setdefault(_word, 0) + 1

result = sorted(qty_words, key=qty_words.get, reverse=True)

print(f'10 самых частых слов: {result[:FRE_WORDS]}')

