# Чернеги Вікторії   Б19_д/122Б
'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
'''

import numpy as np                                  # імпортування бібліотек
import random

array = np.zeros(20, dtype = int)                   # масив, заповнений нулями типу int
sum = 0                                             # змінна, шо позначає суму парних елементів
for i in range(len(array)):                         # цикл для заповнення масиву елементами
    array[i] = random.randint(100, 200)             # внесення рандомних елементів в діапазоні від 100 до 200 в масив
print(array)                                        # виведення масиву
for i in range(len(array)):                         # цикл для проходження по елементам масиву
    if array[i]%2 == 0:                             # перевірка на парність елементу
        sum += array[i]                             # якщо елемент парний, то він додається до суми
print(f'Amount of binate numbers: {sum}')           # виведення суми парних елементів