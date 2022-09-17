# Задача №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# my_str = 'абвгдейка, абвгдейка - это учеба и игра'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))
#---------------------------------------------

# Задача №4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Файл с исходными данными input.txt. Файл со сжатыми данными output.txt

# def compressing(data):
#     c = 1
#     res = ''
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]:
#             c += 1
#         else:
#             res = res + str(c) + data[i]
#             c = 1
#     if c > 1 or (data[len(data)-2] != data[-1]):
#         res = res + str(c) + data[-1]
#     return res

# def decompressing(data):
#     number = ''
#     res = ''
#     for i in range(len(data)):
#         if not data[i].isalpha():
#             number += data[i]
#         else:
#             res = res + data[i] * int(number)
#             number = ''
#     return res

# # сжатие и запись в файл output.txt
# d1=open('input.txt', 'r')
# s1=(''.join(d1.readlines()))

# rec=open('output.txt', 'w')
# rec.write(compressing(s1))
# rec.close()

# # восстановление и запись в файл outputresurrect.txt
# d2=open('output.txt', 'r')
# s2=(''.join(d2.readlines()))

# resurr=open('outputresurrect.txt', 'a+')
# resurr.write(decompressing(s2))
# resurr.close()
#---------------------------------------------

# Задача №2: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета... 

# Я не хочу писать код про конфеты. Кроме того, 2021 конфета! Вы представляете, сколько ходов должны сделать игроки?
# Они быстрее умрут от старости, чем закончат игру. Код будет про игру в монетки. Условие игры в теле кода.
 
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество монет, которое возьмете (от 1 до 3): "))
    while x < 1 or x > 3:
        x = int(input(f"{name}, введите корректное количество монет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Походил {name}, он взял {k} монеты(у), теперь у него {counter} монет(ы). Осталось на столе {value} монет(ы).")

print("На столе 11 монет. Каждый игрок берет от 1 до 3 монет. Проигрывает взявший последнюю монету.")
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 11 # стартовое количество монет
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 1:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player2}")
else:
    print(f"Выиграл {player1}")