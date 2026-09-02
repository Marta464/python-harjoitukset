oikea_nimi = "python"
oikea_salasana = "rules"

yritykset = 0

nimi = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
yritykset = yritykset + 1 

while (nimi != oikea_nimi or salasana != oikea_salasana) and yritykset < 5:
    print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
    
    
    nimi = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset = yritykset + 1


if nimi == oikea_nimi and salasana == oikea_salasana: 
    print("Tervetuloa")
else:
    print("Pääsy evätty")