# Спрашиваем основание и высоту у пользователя
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Считаем площадь (pinta-ala) и периметр (piiri)
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

# Выводим результаты красивыми f-строками с округлением
print(f"Suorakulmion pinta-ala: {pinta_ala:.2f}")
print(f"Suorakulmion piiri: {piiri:.2f}")
