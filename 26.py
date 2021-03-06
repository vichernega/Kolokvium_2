# Чернеги Вікторії   Б19_д/122Б
'''
Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у масив T.
'''

import numpy as np                                              # імпортування бібліотеки

temperature = np.zeros(6, dtype = float)                        # масив заповнений нулями типу float
sum = 0                                                         # змінна для позначення суми всіх елементів масиву
for i in range(len(temperature)):                               # цикл для заповнення масиву користувачем
    temperature[i] = float(input(f'Temperature №{i}: '))        # заповнення масиву
    sum += temperature[i]                                       # додавання всіх елементів масиву, щоб потім знайти середнє значення
print(temperature)                                              # виведення масиву
print(f'Min temperature is {min(temperature)}')                 # виведення мінімального значення масиву
print(f'Max temperature is {max(temperature)}')                 # виведення максимального значення масиву
print(f'Average temperature is {sum/len(temperature)}')         # виведення середнього арифметичного значенння масиву