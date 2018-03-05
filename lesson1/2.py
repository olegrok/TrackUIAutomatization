#!/usr/bin/python3

# Создайте массив целых чисел (размер 7 элементов),
# заполните его только четными числами,
# а затем каждый второй элемент умножьте на предыдущий

import random

# Размер массива
N = 7

# Ограничение на размер элементов в массиве. Не больше чем 2*HalfMax
HalfMax = 100

array = [2 * random.randint(0, HalfMax) for i in range(N)]
print("Исходный массив:", array)
for i in range(N):
    if i % 2 == 0 and i != 0:
        array[i] *= array[i - 1]
print("Итоговый массив:", list(array))
