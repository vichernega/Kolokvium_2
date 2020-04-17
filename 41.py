# Чернеги Вікторії   Б19_д/122Б
'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
'''

import numpy as np                                          # імпортування бібліотек
import random

a = int(input('Your number: '))                             # введення числа, з яким буде порівнюватись максимальне значення масиву
n = int(input('Quantity of elements in array: '))           # кількість елементів масиву(задає користувач)
array = np.zeros(n, dtype = int)                            # масив, заповнений нулями
count =  0                                                  # лічильник кількості максимальних елементів
for i in range(len(array)):                                 # цикл для проходження по елементам масиву
    array[i] = random.randint(-10, 10)                      # заповнення масиву числами від -10 до 10 рандомно
print(array)                                                # виведення масиву
for i in range(len(array)):                                 # цикл для проходження по елементам масиву, щоб дізнатись кількість елементів, що мають максимальне значення
    if max(array) == array[i]:                              # якщо максимальний елеент дорівнює елементу на позиції і, то до лічильника додається 1
        count += 1
if a < max(array) or count >= 2 :                           # якщо максимальне значення розташоване на декількох позиціях чи макс елемент більший заданого числа, то t приймає значення хиба
    t = False
else:                                                       # в іншому випадку t - істина
    t = True
print(t)                                                    # виведення значення t