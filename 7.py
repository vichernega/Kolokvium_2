# Чернеги Вікторії   Б19_д/122Б
'''
Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0.
'''

import numpy as np                                      # імпортування бібліотек
import random

A = np.zeros(12, dtype = int)                           # масив, заповнений нулями
for i in range(len(A)):                                 # цикл для проходження по елементам масиву
    A[i] = random.randint(-20, 10)                      # заповнення масиву числами від -20 до 10 рандомно
print(A)                                                # виведення масиву
for i in range(len(A)):                                 # цикл для проходження по елементам масиву
    if A[i] < 0:                                        # умова від'ємності елементу масиву
        A[i] = 0                                        # заміна від'ємних елементів на 0
print(A)                                                # виведення масиву із заміненими елементами