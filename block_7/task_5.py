print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

a = int(input('Введите нижний предел отрезка: '))
b = int(input('Введите верхний предел отрезка: '))
total, cnt = 0, 0
for number in range(a, b + 1):
    if number % 3 == 0:
        total += number
        cnt += 1
print('Среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3:', total / cnt)

