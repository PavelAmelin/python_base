print('Задача 1. Тестовое задание')

# Степан пришёл устраиваться на работу, где ему дали тестовое задание:
# проанализировать такую таблицу,
# понять как она строится и написать программу для вывода её на экран.

# 0 2 4 6  8  10
# 1 3 5 7  9  11
# 2 4 6 8  10 12
# 3 5 7 9  11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15
#
# Помогите Степану реализовать такую программу.
# Подсказка: номера столбцов. А ещё не забудьте про литерал \t для табуляции

size = int(input('Введите размер матрицы: '))
for i in range(size):
    for j in range(size):
        print(i + 2 * j, end='\t')
    print()
