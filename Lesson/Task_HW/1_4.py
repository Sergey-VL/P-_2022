# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

num = int(input("Введите номер четверти: "))
if num > 0 and num < 5:
    if num == 1:
        print("Диапазон: x > 0, y > 0")
    if num == 2:
        print("Диапазон: x < 0, y > 0")
    if num == 3:
        print("Диапазон: x < 0, y < 0")
    if num == 4:
        print("Диапазон: x > 0, y < 0")
else:
    print("Такой четверти нет")
