# Чернеги Вікторії   Б19_д/122Б
'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
'''

import numpy as np                                  # імпортування бібліотек
import random

array = np.zeros(10, dtype = int)                   # масив, заповнений нулями типу int
dob = 1                                             # змінна, шо позначає добуток елементів, кратних 3 і 9
for i in range(len(array)):                         # цикл для заповнення масиву елементами
    array[i] = random.randint(5, 500)               # внесення рандомних елементів в діапазоні від 5 до 500 в масив
print(array)                                        # виведення масиву
for i in range(len(array)):                         # цикл для проходження по елементам масиву
    if array[i]%3 == 0 and array[i]%9 == 0:         # перевірка чи є елементи, що діляться на 3 і 9 націло. Якщо є, вони перемножуються
        dob *= array[i]
if dob == 1:                                        # якщо елементів, що ділятьчя на 3 і 9 немає, виведення інформації про це
    print(f'There is no such numbers')
else:                                               # якщо є такі елементи, виведення їх добутку
    print(f'Composition of such elements: {dob}')