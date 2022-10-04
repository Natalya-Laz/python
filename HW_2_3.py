
# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input("Введите число: "))
list_number = []
i = 0

for i in range(1, n + 1):
    i += 1
    x = ((1 + 1 / i) ** i)
    list_number.append(x)
print(F"{list_number}")

summa = 0
for i in range(0, len(list_number)):
    summa += list_number[i]
print(f"Сумма= {summa}")