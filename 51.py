# Чернеги Вікторії   Б19_д/122Б
'''
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
'''

import numpy as np                                          # імпортування бібліотек
import random

n = int(input('Quantity of elements in array: '))           # кількість елементів масиву(задає користувач)
array, array1 = np.zeros(n, dtype = int), []                # масив, заповнений нулями та пустий список
for i in range(len(array)):                                 # цикл для проходження по елементам масиву
    array[i] = random.randint(0, 100)                       # заповнення масиву числами від 0 до 100 рандомно
    if array[i] - i == 10:                                  # якщо елемент перевищує свій номер на 10, то він додається у список
        array1.append(array[i])
print(array)                                                # виведення масиву
if array1 == []:                                            # якщо список пустий, виводиться інформація про те, що у масиві немає елементів, що перевищували б свій номер на 10
    print('There is no such elements')
else:                                                       # в іншому випадку виводиться список з елементів, що задовільняють умову, перетворений у масив
    print(np.array(array1))
