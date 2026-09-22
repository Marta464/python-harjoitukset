class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa nyt {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa!")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print("Virhe: Kyseistä kerrosta ei ole olemassa.")
            return

        print(f"\n--- Siirrytään kerrokseen {kohde_kerros} ---")
        
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        
        self.hissit = []
        
        for i in range(hissien_maara):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, hissin_numero, kohde_kerros):
        valittu_hissi = self.hissit[hissin_numero - 1]
        valittu_hissi.siirry_kerrokseen(kohde_kerros)


talo = Talo(1, 7, 2)

talo.aja_hissia(1, 5) 
talo.aja_hissia(2, 3)
