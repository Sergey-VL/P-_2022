# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

# import random - второй способ вызова модуля через точечную нотацию, то есть в теле цикла надо было писать random.sample(range(......))
from random import sample      # один из способов вызова модуля(random) для использования функции sample - она возвращает список

def find_num (amount, user_num):
    new_list = sample(range(1,(amount+1)*2), k=amount)  # создание списка, k - параметр сколько функция возмет случайных значений из набора
    print(new_list)
    if user_num in new_list:
        return 'yes'
    return 'no'

some_num = find_num(int(input("Введите amount: ")),      # поместили нашу функцию(def) в переменную  и потом печатаем её,
                                                        # что бы можно было выввести на экран return
                    int(input("Введите user_num: ")))
print(some_num)
