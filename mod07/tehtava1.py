import random

def heitta ():
    """Palauttaa satunnaisen nopan silmäluvun välitä 1-6."""
    return random.randint(1, 6)

#Pääphjelma
def main():
    while True:
        silmaluku = heitta()
        print(f"Heitit: {silmaluku}")

        if silmaluku == 6:
            print("Sait kuutosen, peli päättyy!")
        break

if __name__ == "__main__":
    main()