# Чернеги Вікторії   Б19_д/122Б
'''
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
'''

array = ['Smith', 'Jonhson', 'Williams', 'Brown', 'Jones']                  # заданий масив
letter = input('Input the first letter (uppercase): ')                      # введення букви користувачем
for i in range(len(array)):                                                 # цикл для проходження по словам масиву
    for j in range(len(array[i])):                                          # цикл для проходження по буквам слів
        if letter == array[i][j]:                                           # умова збігу першої букви в прізвищі та введеної користвачем букви
            print(f'Surname {array[i]} is started from letter {letter}')    # виведення прізвища у разі збігу букв
