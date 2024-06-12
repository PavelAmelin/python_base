text = input('Введите текст: ')
position = 1
for symbol in text:
    if symbol == '*':
        print('Символ «*» стоит на позиции', position)
    position += 1
