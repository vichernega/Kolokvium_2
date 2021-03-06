# Чернеги Вікторії   Б19_д/122Б
'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
'''

import numpy as np                                          # імпортування бібліотек
import random

n = int(input('Quantity of elements in array: '))           # кількість елементів масиву(задає користувач)
array = np.zeros(n, dtype = int)                            # масив, заповнений нулями
a, b = 0, 0                                                 # змінні, яким буде присвоюватись додатнє і від'ємне значення
for i in range(len(array)):                                 # цикл для проходження по елементам масиву
    array[i] = random.randint(-10, 10)                      # заповнення масиву числами від -10 до 10 рандомно
    if array[i] < 0:                                        # якщо елемент масиву більше нуля, то його значення присвоюється змінній
        a = array[i]
    elif array[i] > 0:                                      # якщо елемент масиву менший нуля, то його значення присвоюється змінній
        b = array[i]
print(array)                                                # вивід масиву
if a == 0 or b == 0:                                        # якщо хоча б одна змінна не змінила своє значення від нуля, то t приймає значення хиба
    t = False
else:                                                       # в іншому випадку t - істина
    t = True
print(t)                                                    # виведення значення t