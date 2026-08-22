# 1. Спрашиваем у пользователя средневековые меры веса
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

# 2. Переводим каждую меру в чистые граммы по условию задачи:
# 1 luoti = 13.3 грамма
luoti_grammoina = luoti * 13.3

# 1 naula = 32 luotia = 32 * 13.3 грамма
naula_grammoina = naula * 32 * 13.3

# 1 leiviskä = 20 naulaa = 20 * 32 * 13.3 грамма
leiviska_grammoina = leiviska * 20 * 32 * 13.3

# 3. Считаем общий вес в граммах (складываем всё вместе)
yhteisgrammat = luoti_grammoina + naula_grammoina + leiviska_grammoina

# 4. Выделяем килограммы и оставшиеся граммы с помощью специальной математики Python:
# // — это деление нацело (узнаем сколько ровно тысяч граммов помещается в числе)
kilogrammat = int(yhteisgrammat // 1000)

# % — это остаток от деления (узнаем сколько граммов осталось после того, как забрали кг)
grammat = yhteisgrammat % 1000

# 5. Выводим результат в точности по шаблону учителя
print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
