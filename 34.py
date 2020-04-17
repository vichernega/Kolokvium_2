# Чернеги Вікторії   Б19_д/122Б
'''
Дано два лінійних масиви однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
'''

import numpy as np                                          # імпортування бібліотек
import random

n = int(input('Quantity of elements in array: '))           # кількість елементів масиву(задає користувач)
array1, array2, array3 = np.zeros(n, dtype = int), np.zeros(n, dtype = int), np.zeros(n, dtype = int)     # масиви, заповнені нулями і один пустий
for i in range(len(array1)):                                 # цикл для проходження по елементам масивів
    array1[i] = random.randint(-10, 10)                      # заповнення масиву числами від -10 до 10 рандомно
    array2[i] = random.randint(-10, 10)                      # заповнення масиву числами від -10 до 10 рандомно
    array3[i] = array1[i] * array2[i]                        # заповнення третьго масиву добутками елементів першого і другого масивів
print(f'The first array: {array1}')                          # виведення 1 масиву
print(f'The second array: {array2}')                         # виведення 2 масиву
print(f'The third array: {array3}')                          # виведення 3 масиву