# # 2. Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dictionary = {}
i = 1
n = int(input("Введите число = "))
for i in range(1, n+1):
    index = i
    value = 3 * i + 1
    dictionary[index] = value
    i += 1
print(f"{dictionary} ", end=" ")











