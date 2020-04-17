# Чернеги Вікторії   Б19_д/122Б
'''
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
'''

temperature = [1, -2, -15, -23, -11, -3, -1, -5, -6, -7]                # масив з температурами
count = 0                                                               # змінна для рахунку кількості температур
for i in range(len(temperature)):                                       # цикл для проходження по масиву
    if temperature[i]<-10:                                              # умова, при якій температура нище -10
        count += 1                                                      # якщо умова виконується, до лічильника додається 1
print(f'The temperature has fallen below minus ten {count} times')      # вивід кількості температур нище -10