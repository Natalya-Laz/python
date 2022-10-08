# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal
def accuracy (num, acc):
    number = Decimal(f" {num} ")
    return number.quantize(Decimal(f"{acc}"))
print(accuracy(float(input("Введите число: ")),float(input("Введите необходимую точность: "))))



