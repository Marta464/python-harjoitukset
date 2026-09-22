import random

# Part 1
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.kuljettu_matka = self.kuljettu_matka + (self.tämänhetkinen_nopeus * tuntimäärä)


# Part 2
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


# Part 3
sahko = Sähköauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.kiihdytä(120)
bensa.kiihdytä(100)

sahko.kulje(3)
bensa.kulje(3)

print(f"Sähköauto ({sahko.rekisteritunnus}) ajoi: {sahko.kuljettu_matka} km")
print(f"Polttomoottoriauto ({bensa.rekisteritunnus}) ajoi: {bensa.kuljettu_matka} km")