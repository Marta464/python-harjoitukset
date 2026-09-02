class Auto:
    
    def __init__(self, rekisteritunnus, huippunopeus):
        
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        
        
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

uusi_auto = Auto("ABC-123", 142)

print("Uuden auton tiedot:")
print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
print(f"Huippunopeus: {uusi_auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {uusi_auto.tämänhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")

uusi_auto.kiihdytä(30)
uusi_auto.kiihdytä(70)
uusi_auto.kiihdytä(50)

print(f"Nopeus kiihdytysten jälkeen: {uusi_auto.tämänhetkinen_nopeus}")
uusi_auto.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.tämänhetkinen_nopeus}")