# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
n = int(input())
for n in range(1, n+1):
    num_list.append((1+1/n)**n)
num_list = [round(v,3) for v in num_list]
print(num_list)
sum = 0
for i in num_list:
    sum += i
print(round(sum, 3))