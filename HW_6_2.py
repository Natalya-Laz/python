# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
from random import randint
list_1 = [randint(1, 100) for i in range(randint(5, 10))]
print(list_1)
print(sum([list_1[i] for i in range(1, len(list_1), 2)]))
