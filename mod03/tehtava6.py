import random

# 1. Генерируем 3 случайные цифры от 0 до 9 для первого кода
koodi1_osa1 = random.randint(0, 9)
koodi1_osa2 = random.randint(0, 9)
koodi1_osa3 = random.randint(0, 9)

# 2. Генерируем 4 случайные цифры от 1 до 6 для второго кода
koodi2_osa1 = random.randint(1, 6)
koodi2_osa2 = random.randint(1, 6)
koodi2_osa3 = random.randint(1, 6)
koodi2_osa4 = random.randint(1, 6)

# 3. Выводим коды на экран, склеивая цифры вместе в одну строчку
print(f"3-numeroinen koodi (0-9): {koodi1_osa1}{koodi1_osa2}{koodi1_osa3}")
print(f"4-numeroinen koodi (1-6): {koodi2_osa1}{koodi2_osa2}{koodi2_osa3}{koodi2_osa4}")
