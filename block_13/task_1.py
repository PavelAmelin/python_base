print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введитечисло: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

def convert_num(number):
    cnt = 0
    if number >= 1:
        while number > 10:
            cnt += 1
            number /= 10
        return f'Формат плавающей точки: x = {number} * 10 ** {cnt}'
    elif 0 < number < 1:
        while number < 1:
            cnt += 1
            number *= 10
        return f'Формат плавающей точки: x = {round(number, 2)} * 10 ** -{cnt}'
    return 'Ошибка ввода, число должно быть больше 0'

N = float(input('Введите число: '))
print(convert_num(N))


