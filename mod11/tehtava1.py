class Julkaisu:
    def __init__ (self, nimi):
            self.nimi = nimi

class Kirja(Julkaisu):
    def __init__ (self, nimi, kirjalija, sivumäärä):
            super().__init__(nimi)
            self.kirjalija = kirjalija
            self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjalija}")
        print(f"Sivumäärä: {self.sivumäärä} sivua\n")

class Lehti(Julkaisu):
    def __init__ (self, nimi, päätoimittaja):
            super().__init__(nimi)
            self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}\n")

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print("--- Julkaisujen tiedot ---\n")
lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()