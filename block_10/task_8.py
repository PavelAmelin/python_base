print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

size = int(input('Введите число: '))
for i in range(1, size + 1):
    for j in range(i):
        print(size - j, end='')
    for j in range(size - i):
        print('.', end='')
    for j in range(size - i):
        print('.', end='')
    for j in range(i):
        print(size + 1 - (i - j), end='')
    print()
