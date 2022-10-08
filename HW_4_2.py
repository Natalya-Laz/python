# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа

n = int(input("Введите число : "))
print(n)
count = 0
lst = []
while n != count:
    if n % 2 == 0:
        n = n // 2
        lst.append(2)
    elif n % 3 == 0:
        n = n // 3
        lst.append(3)
    elif n % 5 == 0:
        n = n // 5
        lst.append(5)
    elif n != 0:
        lst.append(n)
        count = n
print(lst)