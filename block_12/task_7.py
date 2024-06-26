print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors(item_comp):
    item_human = input('Введите предмет к(камень), н(ножницы) или б(бумага): ')
    if item_human == 'к' and item_comp == 'н' or item_human == 'н' and item_comp == 'б' or item_human == 'б' and item_comp == 'к':
        print('Вы победили')
    elif item_human == 'н' and item_comp == 'к' or item_human == 'б' and item_comp == 'н' or item_human == 'к' and item_comp == 'б':
        print('Вы проиграли')
    elif item_human == 'н' and item_comp == 'н' or item_human == 'б' and item_comp == 'б' or item_human == 'к' and item_comp == 'к':
        print('Введите еще раз: ')
        rock_paper_scissors(item_comp)
    else:
        print('Ошибка ввода')
        rock_paper_scissors(item_comp)

def guess_the_number(guess):
    cnt = 0
    while True:
        num = int(input('Введите число от 0 до 1000: '))
        cnt += 1
        if num < guess:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        elif num > guess:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        else:
            break
    print('Вы угадали! Число попыток:', cnt)

def main_menu():
    choice = int(input('Выберите игру, 1 игра "Камень, ножницы, бумага", 2 игра “Угадай число”: '))
    if choice == 1:
        our_item_comp = random.choice(['к', 'н', 'б'])
        rock_paper_scissors(our_item_comp)
    elif choice == 2:
        our_guess = random.randint(0, 1000)
        guess_the_number(our_guess)
    else:
        print('Такой игры не существует')
        main_menu()


main_menu()
