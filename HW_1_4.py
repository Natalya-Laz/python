import math
xa = int(input("Введите координату  Х для первой точки"))
ya = int(input("Введите координату  Y для первой точки"))
xb = int(input("Введите координату  Х для второй точки"))
yb = int(input("Введите координату  Х для второй точки"))
print("Растояние между двумя точками",(round(math.sqrt((xa-xb)**2 + (ya-yb)**2),2)))


