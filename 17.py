# Чернеги Вікторії   Б19_д/122Б
'''
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100 до 200.
'''

import numpy as np                                  # імпортування бібліотек
import random

array = np.zeros(20, dtype = float)                 # масив, заповнений нулями типу float
sum = 0                                             # змінна, шо позначає суму елементів на непарних позиціях
for i in range(len(array)):                         # цикл для заповнення масиву елементами
    array[i] = random.uniform(100,200)              # внесення в масив рандомних значень типу float в діапазоні від 100 до 200
print(array)                                        # виведення масиву
for i in range(1, len(array), 2):                   # проходження по елементам масиву через один, починаючи з 1 (тобто по індексам 1, 3, 5, 7, 9)
    sum += array[i]                                 # додавання елементів, що відповідають непарним індексам
print(f'Amount: {sum}')                             # виведення суми