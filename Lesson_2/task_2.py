# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from math import gcd
import fractions
 
a1, b1 = map(int, input("Введите дробь вида “a/b: ").split('/'))
a2, b2 = map(int, input("Введите дробь вида “a/b: ").split('/'))

f1 = fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2)
print(f"Проверка сложения: {f1}")
f2 = fractions.Fraction(a1, b1) * fractions.Fraction(a2, b2)
print(f"Проверка умножения: {f2}")
 
denominator = int(b1*b2/gcd(b1, b2))
numerator = int(denominator/b1*a1+denominator/b2*a2)
num = gcd(numerator, denominator)
n = int(numerator/num)
d = int(denominator/num)
print('Сумма дробей: {}/{}'.format(n, d) if n != d else n)

denominator1 = int(b1 * b2)
numerator2 = int(a1 * a2)
num2 = gcd(numerator2, denominator1)
n2 = int(numerator2/num2)
d2 = int(denominator1/num2)
print('Произведение дробей: {}/{}'.format(n2, d2) if n2 != d2 else n2)
