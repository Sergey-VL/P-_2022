# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import sample   # подключение модуля(random) для использования функции sample - она перемешивает

def words_list (num, word="abc"): # создаем  функцию, она будет создавать список слов,
                                  # num - кол-во слов, word - переменная которая принимает строку abc которая будет перемешиваться
    w_list = []   # создаем пустой список для слов
    for i in range(num):
        m = sample(word, k=3) # список букв
        w_list.append("".join(m)) # создание списка  и создание слов внутри списка , join - склеивание , используется только для типа строк
    return w_list

def find_second (n_list, word):  # нахождение кол-ва вхождений и на каком индексе, word - это переменная, где будет слово которое будем искать
    if word in n_list and n_list.count(word) > 1:
        c = n_list.index(word) # нахождение индекса первого вхождения
        print(n_list.index(word, c+1)) # нахождение индекса второго вхождения
    else:
        print(-1) # указывает что вхождения или второго вхождения нет


n = int(input('Введите число: '))
u = words_list(n)
print(u)
w = input("Введите слово: ")
find_second(u, w)
