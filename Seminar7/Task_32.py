#  Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

arr = [] 
size = int(input("Введите длину массива: "))
for i in range(size):
    arr.append(random.randint(-8, 10))

print(arr)

min1 = int(input("Введите min значение: "))
max1 = int(input("Введите max значение: ")) 
for i in range(len(arr)):
    if min1 <= arr[i] <= max1: 
        print(i)