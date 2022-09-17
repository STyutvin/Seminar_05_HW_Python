# Задача №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# my_str = 'абвгдейка, абвгдейка - это учеба и игра'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))
#---------------------------------------------

# Задача №4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Файл с исходными данными input.txt. Файл со сжатыми данными output.txt

def compressing(data):
    c = 1
    res = ''
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            c += 1
        else:
            res = res + str(c) + data[i]
            c = 1
    if c > 1 or (data[len(data)-2] != data[-1]):
        res = res + str(c) + data[-1]
    return res

def decompressing(data):
    number = ''
    res = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            res = res + data[i] * int(number)
            number = ''
    return res

# сжатие и запись в файл output.txt
d1=open('input.txt', 'r')
s1=(''.join(d1.readlines()))

rec=open('output.txt', 'w')
rec.write(compressing(s1))
rec.close()

# восстановление и запись в файл outputresurrect.txt
d2=open('output.txt', 'r')
s2=(''.join(d2.readlines()))

resurr=open('outputresurrect.txt', 'a+')
resurr.write(decompressing(s2))
resurr.close()