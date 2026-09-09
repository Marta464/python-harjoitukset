import random

def heitta ():
    """Palauttaa satunnaisen nopan silmäluvun välitä 1-21."""
    return random.randint(1, 21)

#Pääphjelma
def main():
    while True:
        silmaluku = heitta()
        print(f"Heitit: {silmaluku}")

        if silmaluku == 21:
            print("Sait kuutosen, peli päättyy!")
        break

if __name__ == "__main__":
    main()