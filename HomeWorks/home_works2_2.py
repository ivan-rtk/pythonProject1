"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление.
Функцию hex используйте для проверки своего результата."""

our_hex = int(input('Введите число: '))
result = ''
DIVIDER = 16
print(hex(our_hex))
while our_hex > 0:
    result = str(our_hex % DIVIDER) + result
    our_hex //= DIVIDER
print(result)
