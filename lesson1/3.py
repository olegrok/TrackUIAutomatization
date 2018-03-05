#!/usr/bin/python3

# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы


def count_numbers(x):
    if x == 0:
        return 0
    return (x % 10) + count_numbers(x // 10)


x = int(input())
print("Вы ввели:", x)
print("Ответ:", count_numbers(x))
