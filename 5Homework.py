# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import random
print('Задача 1.')
some_text = 'Здесь должен быть бытабв некоторый некоторыйабв текст, который необходимо вести!'


def del_words(some_text):
    some_text = list(filter(lambda x: 'абв' not in x, some_text.split()))
    return " ".join(some_text)


some_text = del_words(some_text)
print(some_text)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# 1. человек/человек
print('_____________________________________________')
print('Задача 2.1\nЧеловек/Человек')
k = int(30)
# ost = k % 29
# print(ost)
m = 28
print(
    f'На столе лежит {k} конфет. За один ход можно забрать не более чем {m} конфет. Первый ход определяется жеребьёвкой.')
player1_turn = int(0)
player2_turn = int(1)
turn = random.randint(0, 1)
while k > 0:
    if turn == 0:
        print('Ход делает Игрок №1')
        k1 = int(input('Сколько конфет хотите взять? '))
        if k1 > k or k1 > m:
            print('Вы взяли слишком много конфет, попробуйте еще раз! ')
        else:
            k = k - k1
            if k == 0:
                print('Выйграл Игрок №1!')
            else:
                print(f'Осталость {k}')
            turn = 1
    else:
        print('Ход делает Игрок №2')
        k2 = int(input('Сколько конфет хотите взять? '))
        if k2 > k or k2 > m:
            print('Вы взяли слишком много конфет, попробуйте еще раз! ')
        else:
            k = k - k2
            if k == 0:
                print('Выйграл Игрок №2!')
            else:
                print(f'Осталость {k}')
            turn = 0

# 2. человек/бот
print('_____________________________________________')
print('Задача 2.2\nЧеловек/бот')
k = int(100)
# ost = k % 29
# print(ost)
m = 28
print(
    f'На столе лежит {k} конфет. За один ход можно забрать не более чем {m} конфет. Первый ход определяется жеребьёвкой.')
player1_turn = int(0)
player2_turn = int(1)
turn = random.randint(0, 1)
while k > 0:
    if turn == 0:
        print('Ход делает Игрок №1')
        k1 = int(input('Сколько конфет хотите взять? '))
        if k1 > k or k1 > m:
            print('Вы взяли слишком много конфет, попробуйте еще раз! ')
        else:
            k = k - k1
            if k == 0:
                print('Выйграл Игрок №1!')
            else:
                print(f'Осталость {k}')
            turn = 1
    else:
        print('Ход делает компьютер')
        if k > m:
            k2 = random.randint(1, m)
        else:
            k2 = random.randint(1, k)
        print(f'Компьютер взял {k2}')
        k = k - k2
        if k == 0:
            print('Выйграл компьютер!')
        else:
            print(f'Осталость {k}')
        turn = 0

# 3. человек/умный бот
print('Задача 2.3\nЧеловек/Умный бот')
k = int(100)
# ost = k % 29
m = 28
print(
    f'На столе лежит {k} конфет. За один ход можно забрать не более чем {m} конфет. Первый ход определяется жеребьёвкой. Все конфеты оппонента достаются сделавшему последний ход')
player1_turn = int(0)
player2_turn = int(1)
turn = random.randint(0, 1)
while k > 0:
    if turn == 0:
        print('Ход делает Игрок №1')
        k1 = int(input('Сколько конфет хотите взять? '))
        if k1 > k or k1 > m:
            print('Вы взяли слишком много конфет, попробуйте еще раз! ')
        else:
            k = k - k1
            if k == 0:
                print('Выйграл Игрок №1!')
            else:
                print(f'Осталость {k}')
            turn = 1
    else:
        print('Ход делает компьютер')
        if k > m:
            if k % (m+1) == 0:
                k2 = m
            else:
                k2 = k % (m + 1)
        else:
            k2 = k
        print(f'Компьютер взял {k2}')
        k = k - k2
        if k == 0:
            print('Выйграл компьютер!')
        else:
            print(f'Осталость {k}')
        turn = 0

# 3. Создайте программу для игры в ""Крестики-нолики"".
print('_____________________________________________')
print('Задача 3')


def wins_X(game):
    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        print('X выйграли!')
        return True
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        print('X выйграли!')
        return True
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        print('X выйграли!')
        return True
    elif game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        print('X выйграли!')
        return True
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        print('X выйграли!')
        return True
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        print('X выйграли!')
        return True
    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        print('X выйграли!')
        return True
    elif game[2][0] == 'X' and game[1][1] == 'X' and game[0][2] == 'X':
        print('X выйграли!')
        return True
    else:
        return False


def wins_O(game):
    if game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        print('O выйграли!')
        return True
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        print('O выйграли!')
        return True
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        print('O выйграли!')
        return True
    elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        print('O выйграли!')
        return True
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        print('O выйграли!')
        return True
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        print('O выйграли!')
        return True
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        print('O выйграли!')
        return True
    elif game[2][0] == 'O' and game[1][1] == 'O' and game[0][2] == 'O':
        print('O выйграли!')
        return True
    else:
        return False


game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],]
for i in game:
    print(i)
while not wins_X(game) and not wins_O(game):
    a, b = int(input('Введите номер строки от 0 до 2 куда хотите походить')), int(
        input('Введите номер столбца от 0 до 2 куда хотите походить'))
    while game[a][b] == 'X' or game[a][b] == 'O':
        print('Это поле занято, попробуйте еще раз!')
        a, b = int(input('Введите номер строки от 0 до 2 куда хотите походить')), int(
            input('Введите номер столбца от 0 до 2 куда хотите походить'))
    game[a][b] = 'X'
    for i in game:
        print(i)
    print('ход компьютера')
    while True:
        c, d = random.randint(0, 2), random.randint(0, 2)
        if game[c][d] == ' ':
            break
    game[c][d] = 'O'
    for i in game:
        print(i)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
print('_____________________________________________')
print('Задача 4')
with open('RLE_coding.txt', 'r') as data:
    s = data.read()


def coding(s):
    count = 1
    res = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res = res + str(count) + s[i]
            count = 1
    if count > 1 or (s[len(s)-2] != s[-1]):
        res = res + str(count) + s[-1]
    return res


with open('RLE_decoding.txt', 'r') as data:
    c = data.read()


def decoding(s):
    number = ''
    res = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            number += s[i]
        else:
            res = res + s[i] * int(number)
            number = ''
    return res


cs = coding(s)
dc = decoding(c)
print(f'Текст после сжатия: {cs}')
print(f'Текст после восстановления: {dc}')
