# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import random

list1 = []
for i in range(5):
    n = int(input())
    list1.append(n)
print(list1)
k = len(list1)
for i in range(k):
    if i >= k/2:
        break
    print(list1[i] * list1[-i-1], end=" ")
