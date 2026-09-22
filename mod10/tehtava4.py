import random

from tehtava3 import Auto

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

    def kulje(self, tuntimäärä):
        self.kuljettu_matka = self.kuljettu_matka + (self.tämänhetkinen_nopeus * tuntimäärä)

    autot = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippu = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippu))

    kilpailu_kesken = True
    tunnit = 0
        
    while kilpailu_kesken:
        tunnit += 1

        for auto in autot:            
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_kesken = False

    print(f"Kilpailu päättyi {tunnit} tunnin jälkeen.")
    print("-" * 65)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<10} | Huippunopeus: {auto.huippunopeus:<3} km/h | Nopeus: {auto.tämänhetkinen_nopeus:<3} km/h | Matka: {auto.kuljettu_matka:<8.1f} km")

class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autolista

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n--- Tilanne kilpailussa: {self.nimi} ---")
        print("-" * 65)
        for auto in self.autot:
            print(f"Rekisteri: {auto.rekisteritunnus:<10} | Huippu: {auto.huippunopeus:<3} km/h | "
                  f"Nopeus: {auto.tämänhetkinen_nopeus:<3} km/h | Matka: {auto.kuljettu_matka} km")
        print("-" * 65)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

# 1.Uusi
autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippu))

# 2.
romuralli = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

# 3.
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    tunnit += 1
    
    #
    if tunnit % 10 == 0:
        print(f"\nAikaa kulunut: {tunnit} tuntia")
        romuralli.tulosta_tilanne()

# 4.
print(f"\nKilpailu päättyi! Aikaa kului yhteensä {tunnit} tuntia.")
romuralli.tulosta_tilanne()