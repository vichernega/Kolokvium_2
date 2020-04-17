# Чернеги Вікторії   Б19_д/122Б
'''
Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
'''

import numpy as np                                          # імпортування бібліотек

winds = [list(np.zeros(10, dtype = int)), list(np.zeros(10, dtype = int)), list(np.zeros(10, dtype = int)), list(np.zeros(10, dtype = int))]        # створення двовимірного масиву
count = 0                                                                   # змінна для підрахунку кількостей днів з південним вітром, що перевищує 8 м/с
for i in range(len(winds)):                                                 # цикл для проходження по направленням вітру
    for j in range(10):                                                     # цикл для проходження по дням
        if i == 0:                                                          # заповнення масиву(0 відповідає північному вітру, 1 - південному і так далі)
            winds[i][j] = int(input(f'North wind in day №{j} is '))
        elif i == 1:
            winds[i][j] = int(input(f'South wind in day №{j} is '))
            if winds[i][j] > 8:                                             # якщо елемент масиву більший за 8, то до лічильника додається 1
                count += 1
        elif i == 2:
            winds[i][j] = int(input(f'East wind in day №{j} is '))
        else:
            winds[i][j] = int(input(f'West wind in day №{j} is '))
print(winds)                                                                # виведення масиву
print(f'South wind was stronger than 8 m/s {count} times')                  # виведення кількості разів, коли південний вітер був більше 8 м/с