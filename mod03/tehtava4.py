# 1. Запрашиваем три целых числа у пользователя (через int)
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

# 2. Делаем математические расчёты
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# 3. Выводим результаты на экран
print(f"Lukujen summa (сумма): {summa}")
print(f"Lukujen tulo (произведение): {tulo}")
print(f"Lukujen keskiarvo (среднее): {keskiarvo:.2f}")
