print('Задача 1. Конвертация')


# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например,
# если купить что-то в евро,
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
#
# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
#
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

cost_in_euros = float(input('Введите стоимость покупки в евро: '))
cost_in_dollars = cost_in_euros * 1.25
cost_in_roubles = round(cost_in_dollars * 60.87, 2)
print('Стоимость покупки в рублях:', cost_in_roubles)

