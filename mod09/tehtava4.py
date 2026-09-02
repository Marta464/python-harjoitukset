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
