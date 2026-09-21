class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus



        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = ("ABC-123", 142)
print ("Uuden auton tedot:")
print (f"Rekistreritunnus {uusi_auto.rekisteritunnus}")
print (f"Huippunopeus {uusi_auto.huippunopeus}")
print(f"Tämänhetkinen nopeus: {uusi_auto.tämänhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")