# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from time import time

lister = []
n = int(input())
for n in range(0, n):
    lister.append(n)
print(lister)

def mix_list(old: list) -> list:
    new = []
    while old:
        x = str(time()).split('.')[1]
        x = list(map(int, [x[0], x[-1]]))
        x = x[0] if x[0] <= x[1] else x[1]
        if x > len(old)-1:
            new.append(old.pop(0))
        else:
            new.append(old.pop(x))
    return new

lister = mix_list(lister)
print(lister)