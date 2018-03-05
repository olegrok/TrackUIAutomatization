#!/usr/bin/python3

# Дан двумерный массив,
# необходимо вывести двумерный массив у которого четные строки отсортированы по возрастанию, а нечетные по убыванию.
# Так же в консоль необходимо вывести количество итераций, которое было потрачено при сортировке.

import numpy as np

# Размер массива
N, M = 3, 4

# Максимальное и минимальное значение в массиве
Min, Max = -100, 100

iteration = 0
array = np.random.randint(Min, Max, (N, M))
print("Исходный массив:\n", array)

for i in range(N):
    for j in range(M):
        for k in range(j + 1, M):
            if i % 2 != 0:
                if array[i][j] > array[i][k]:
                    array[i][j], array[i][k] = array[i][k], array[i][j]
            else:
                if array[i][j] < array[i][k]:
                    array[i][j], array[i][k] = array[i][k], array[i][j]
            iteration += 1

print("Результат:\n", array)
print("Достигнут за {} итераций".format(iteration))
