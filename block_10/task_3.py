print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

width = int(input('Введите ширину рамки: '))
height = int(input('Введите высоту рамки: '))
for i in range(height):
    for j in range(width):
        if j == 0 or j == width - 1:
            print('|', end='')
        elif i == 0 or i == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()
