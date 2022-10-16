# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

list1 = []
for i in range(10):
    n = int(input())
    list1.append(n)
print(f"Исходная последовательность: {list1}")
res = []
for i in range(len(list1)):
    count = 0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            count += 1
    if count == 1:
        res.append(list1[i])
print(f"Итоговая последовательность с неповторяющимися элементами: {res}")
