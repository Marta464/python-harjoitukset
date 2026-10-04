kortin_saldo = float(input("Anna kortin saldo: "))
yksi_matka = 3.50
if kortin_saldo >= 2.90:
    loppussa = kortin_saldo - 2.90
    print(f"Matka maksettu. Saldo on nyt: {loppussa} euroa.")
elif kortin_saldo < 2.90:
    print("Rahat eivät riitä. Laitaa rahaa kortiin.")