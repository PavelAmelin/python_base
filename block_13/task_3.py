print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K. Напишите программу, которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse(num):
    result = ''
    while num > 0:
        result += str(num % 10)
        num //= 10
    return int(result)

def reverse_and_sum(num1, num2):
    return f'''\nПервое число наоборот: {reverse(num1)}\nВторое число наоборот: {reverse(num2)}\n 
Сумма: {reverse(num1) + reverse(num2)}\nСумма наоборот: {reverse(reverse(num1) + reverse(num2))}'''

our_number_1 = int(input('Введите первое число: '))
our_number_2 = int(input('Введите второе число: '))
print(reverse_and_sum(our_number_1, our_number_2))
