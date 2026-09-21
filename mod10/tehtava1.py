class Hissi:
    def __init__ (self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
           self.nykyinen_kerros += 1
           print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
           
        else:  print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_ylös(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa nyt {self.nykyinen_kerros}")
                  
        else: print("Hissi on jo alimmassa kerroksessa!")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print("Virhe: Kyseistä kerrosta ei ole olemassa.")
            return

        print(f"\n--- Siirrytään kerrokseen {kohde_kerros} ---")
        
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
            
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

#__pääohjelma

h = Hissi(1, 7)

h.siirry_kerrokseen(5)

h.siirry_kerrokseen(1)