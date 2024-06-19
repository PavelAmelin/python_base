print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

quantity = int(input('Введите количество чисел: '))
max_number = 0
max_sum_of_nums = 0
for _ in range(quantity):
    number = int(input('Введите число: '))
    current_num = number
    sum_of_nums = 0
    while number > 0:
        sum_of_nums += number % 10
        number //= 10
    if sum_of_nums > max_sum_of_nums:
        max_sum_of_nums = sum_of_nums
        max_number = current_num
print('Наибольшее по сумме цифр число:', max_number)
print('Его сумма цифр:', max_sum_of_nums)
