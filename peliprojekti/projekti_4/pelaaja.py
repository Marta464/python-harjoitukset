from typing import List
from huone import Huone
from esine import Esine

class Pelaaja:
    def __init__(self, nimi: str, aloitus_sijanti: Huone ):
        self.nimi: str = nimi
        self.esineet: List[Esine] = []
        self.sijanti: Huone = aloitus_sijanti

    def liiku(self, kohde: Huone) -> None:
        self.sijanti = kohde 

    def keraa_esine(self) -> None:
        if self.sijanti.esine:
            uusi_esine = self.sijanti.esine
            self.esineet.append(uusi_esine)
            self.sijanti.esine = None  #otta objekti mukaan
            print (f"'{uusi_esine.nimi}' on lisätty reppuun!\n")
        else:
            print("Tässä huonessa ei ole esineita.\n")

    def nayta_inventaario(self) -> None:
        print("--REPUN SISÄLTÖ--")
        if not self.esineet:
            print("Reppusi on ttuhjä.")
        else:
            for esine in self.esineer:
                print(f"- {esine}")
            print("-------")