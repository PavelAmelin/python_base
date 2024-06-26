print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def biggest_divider(num1, num2):
    while num1 != 0 and num2 != 0:
        if num2 > num1:
            num2 = num2 % num1
        else:
            num1 = num1 % num2
    print(num2 + num1)

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
print('Наибольший общий делитель двух чисел: ', end='')
biggest_divider(number_1, number_2)



