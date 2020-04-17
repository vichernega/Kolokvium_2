# Чернеги Вікторії   Б19_д/122Б
'''
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
'''

import numpy as np                                              # імпортування бібліотек
import random

N = int(input('Your number of the ticket: '))                   # номер виграшного квитка на думку користувача
tickets, win_tick = np.zeros(100, dtype = int), np.zeros(10, dtype = int)    # масиви всіх квитків та виграшних квитків, заповнені нулями
for i in range(len(tickets)):                                   # цикл для проходження по елементам масиву
    tickets[i] = random.randint(0, 200)                         # заповнення масиву числами від 0 до 200 рандомно
print(tickets)                                                  # виведення масиву з усіма квитками
for i in range(len(win_tick)):                                  # цикл для заповнення масиву з виграшними квитками
    win_tick[i] = random.choice(list(tickets))                  # рандомний вибір елемента з перетвореного у список масиву всіх квитків
print(win_tick)                                                 # виведення масиву з винрашними квитками
if N in win_tick:                                               # перевірка чи є номер квитка, що ввів користувач у масиві з виграшними квитками
    print(f'Ticket {N} is winning one')                         # якщо є, виведення інформаціх про це
else:                                                           # в іншому випадку виведення інформації про протилежне
    print(f'Ticket {N} is not winning one')