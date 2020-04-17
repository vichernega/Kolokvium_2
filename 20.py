# Чернеги Вікторії   Б19_д/122Б
'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
'''

import numpy as np                                  # імпортування бібліотек
import random

n = float(input('Your number: '))                   # число, з яким порівнюються елементи масиву
array = np.zeros(20, dtype = float)                 # масив, заповнений нулями типу float
sum = 0                                             # змінна, шо позначає суму елементів більших за задае число
for i in range(len(array)):                         # цикл для заповнення масиву елементами
    array[i] = random.uniform(50,100)               # внесення в масив рандомних значень типу float в діапазоні від 50 до 100
print(array)                                        # виведення масиву
for i in range(len(array)):                         # цикл для проходження по елементам масиву
    if array[i] > n:                                # якщо елемент масиву більший за заданий, він додається
        sum += array[i]
if sum == 0:                                        # якщо більших елементів ніж задане число немає, виведення інформації про це
    print(f'All the numbers are smaller than {n}')
else:                                               # якщо є такі елементи, виведення їх суми
    print(f'Amount of elements that bigger than {n}: {sum}')