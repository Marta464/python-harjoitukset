import math

# Спрашиваем радиус у пользователя
sade = float(input("Anna ympyrän säde: "))

# Считаем площадь по формуле (Пи умножить на радиус в квадрате)
pinta_ala = math.pi * (sade ** 2)

# Выводим результат с округлением до 2 знаков
print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")
