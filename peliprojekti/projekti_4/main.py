import os
from esine import Esine
from huone import Huone
from pelaaja import Pelaaja


def tarkista_ika(ika):
    # Funktio ottaa iän ja palauttaa arvon True tai False.
    if ika < 12:
        return False
    else:
        return True

def nayta_pisteet(pisteet):
    # Pisteiden tulostusfunktio parametrilla ja paluulla
    print("Ennätyspisteesi ovat:", pisteet, "pistettä.\n")
    return pisteet

def lataa_intro():
    # Lukee historiatiedoston, jossa on täsmälleen määritetty kansio.
    polku = "peliprojekti/projekti_4/intro.txt"
    if not os.path.exists(polku):
        polku = "intro.txt" 
        
    with open(polku, "r", encoding="utf-8") as f:
        teksti = f.read()
    return teksti

def lataa_ohjeet():
    # Sääntötiedoston lukemiseen tarkoitettu funktio
    polku = "peliprojekti/projekti_4/ohjet.txt"
    if not os.path.exists(polku):
        polku = "ohjet.txt"

    with open(polku, "r", encoding="utf-8") as f:
        teksti = f.read()
    return teksti

def laske_voima(paino, ika):
    # Matemaattinen funktio toiselle polulle
    tulos = paino * ika
    return tulos

def laske_luonnon_voima(loistun_tyyppi, pelaajan_ika):
    # Elementtien maagisen voiman laskeminen
    ilmasto_mahti = {
        "Pohjolan Tulva": 25,
        "Ikituli ": 30,
        "Kalliomurska ": 35,
        "Jäätävä Pyörremyrsky": 45
    }
    
    # Tarkistetaan, onko pelaajan syöttämä stihiä meidän sanakirjassa
    if loistun_tyyppi in ilmasto_mahti:
        perusvoima = ilmasto_mahti[loistun_tyyppi]
    else:
        perusvoima = 5 # (Jos pelaaja virheellisesti syöttää tuntemattoman elementin, annetaan vähimmäisvoima)
    # Loitsuvoima (perusvoima + ikäbonus)
    kokonaisvoima = perusvoima + (pelaajan_ika * 1.5)

    return kokonaisvoima
    
#Pääohjelma

def main():
    
    opitut_loitsut = [] # Lista pelaajan oppimista loitsuista
    nimi = input("Anna nimesi: ")
    ika = int(input("Anna ikä: "))

    print("Nimesi:", nimi)
    print("Ikä:", ika)

    if tarkista_ika(ika) == False:
        print("Olet alaikäinen. Ohjelma sammuu.")
        return

    print(lataa_intro())
    print(lataa_ohjeet())

    # Luomme esineet
    avain = Esine("Kulta-avain", 0.2)
    miekka = Esine("Miekka", 3.5)
    pihdit = Esine("Pihdit", 1.0)

    # Huoneet
    aula = Huone("Linnan pääsali", avain)
    luola = Huone("Pimeä lohikäärmeen luola", miekka)
    leiri = Huone("Salametsästäjien leiri", pihdit)

    # Sanakirjan käyttö juonen ja tunnelman tallentamiseen
    huoneiden_kuvaukset = {
        "Linnan pääsali": (
            "\n[ Linnan pääsali ]\n"
            "Aksut suuren ja ikivanshan linnan valtaistuinsaliin. Ilma on kylmä ja kiviset seinät "
            "kuiskivat muinaista taikuutta. Keskellä salia palaa heikko tuli, ja sen loisteessa "
            "lattialla kimmeltää jotain arvokasta ja mystistä..."
        ),
        "Pimeä lohikäärmeen luola": (
            "\n[ Pimeä lohikäärmeen luola ]\n"
            "Laskeudut synkkään ja purevan kylmään luolaan. Ilmassa tuoksuu savu ja vaara. "
            "Luolan perällä näet valtavan rautaisen häkin, jossa salametsästäjät pitävät "
            "luonnon suojelijalohikäärmettä vankina! Häkin ympärillä pyörii ilkeitä konnia vartioimassa saalistaan..."
        ),
        "Salametsästäjien leiri": (
            "\n[ Salametsästäjien leiri ]\n"
            "Saavut salametsästäjien leiriin metsän synkkään laitaan. Alue on täynnä roskia, "
            "tyhjiä häkkejä ja luonnon tuhoamiseen tarkoitettuja julmia ansoja. Konnat suunnittelevat "
            "täällä metsän biomin lopullista tuhoamista, mutta he ovat jättäneet työkalunsa hetkeksi vartioimatta..."
        )
    }

    # 4. Pelitilanteen lataaminen
    aloitus_sijainti = aula
    if os.path.exists("peliprojekti/projekti_4/tallenna.txt"):
        jatketaan = input("Löydettiin tallennettu peli. Haluatko jatkaa? (kyllä/ei): ").strip().lower()
        if jatketaan == "kyllä":
            with open("peliprojekti/projekti_4/tallenna.txt", "r", encoding="utf-8") as f:
                tiedot = f.read().split(",")
                nimi = tiedot[0]
                if len(tiedot) > 1 and tiedot[1] == "Pimeä lohikäärmeen luola":
                    aloitus_sijainti = luola
                elif len(tiedot) > 1 and tiedot[1] == "Salametsästäjien leiri":
                    aloitus_sijainti = leiri
            print("Tervetuloa takaisin,", nimi)

    # Pelitilanteen seuranta (Sanakirja)
    tila = {
        "pisteet": 100,
        "vartijat_voitettu": False
    }


    aloitus_sijainti = aula
    if os.path.exists("peliprojekti/projekti_4/tallenna.txt"):
        jatketaan = input("Löydettiin tallennettu peli. Haluatko jatkaa? (kyllä/ei): ").strip().lower()
        if jatketaan == "kyllä":
            with open("peliprojekti/projekti_4/tallenna.txt", "r", encoding="utf-8") as f:
                tiedot = f.read().split(",")
                nimi = tiedot[0]
                if len(tiedot) > 1 and tiedot[1] == "Pimeä lohikäärmeen luola":
                    aloitus_sijainti = luola
                elif len(tiedot) > 1 and tiedot[1] == "Salametsästäjien leiri":
                    aloitus_sijainti = leiri
            print("Tervetuloa takaisin;", nimi)

    # Pelaajan luominen
    pelaaja = Pelaaja(nimi, aloitus_sijainti)
    peli_kaynnissa = True
    pisteet = 100 # Lähtöpisteet

    # Pelin pääsilmukka
    while peli_kaynnissa:
        print("\nPäävalikko (sijainti:", pelaaja.sijanti.nimi, ") ---")
        print("Komennot: pelaa, liiku, loitsu, pisteet, reppu, pelasta, lopeta")
        
        komento = input("Syötä komento: ").strip().lower()

        if komento == "lopeta":
            with open("peliprojekti/projekti_4/tallenna.txt", "w", encoding="utf-8") as f:
                tavarat = ",".join([e.nimi for e in pelaaja.esineet])
                f.write(pelaaja.nimi + "," + pelaaja.sijanti.nimi + "," + tavarat)
            print("Peli tallennettu!")
            print("Kiitos pelaamisesta! Ohjelma sammuu.")
            peli_kaynnissa = False


        elif komento == "pelaa":
            pelaaja.keraa_esine()

            # Luonnon voimat heräävät huoneissa:
            if pelaaja.sijanti == aula and "ikituli" not in opitut_loitsut:
                opitut_loitsut.append("ikituli")
                print("\n[ MAAGINEN VOIMA AKTIVOITU! ]")
                print("Linnan tulisija roiskahtaa! Opit muinaisen taian: 'Ikituli'!")
                
            elif pelaaja.sijanti == leiri and "pohjolan tulva" not in opitut_loitsut:
                opitut_loitsut.append("pohjolan tulva")
                opitut_loitsut.append("kalliomurska") # Kaksi loitsua leirissä vaihtelun vuoksi
                print("\n[ MAAGINEN VOIMA AKTIVOITU! ]")
                print("Maa tärisee ja joet nousevat! Opit loitsut: 'Pohjolan tulva' ja 'Kalliomurska'!")
                
            elif pelaaja.sijanti == luola and "jäätävä pyörremyrsky" not in opitut_loitsut:
                opitut_loitsut.append("jäätävä pyörremyrsky")
                print("\n[ CLIMATE SUPERPOWER ACTIVATED! ]")
                print("Lohikäärmeen huuto herättää purevan pakkasen! Opit loitsun: 'Jäätävä pyörremyrsky'!")

        elif komento == "loistu":
            if len(opitut_loitsut) == 0:
                print("Et osaa vielä yhtään luonnon supervoimaa. Tutki huoneita komennolla 'pelaa'!")
                continue
            print("Osaat seuraavat mahtavat luonnon voimat:")
            for l in opitut_loitsut:
                print("-", l)
                
            valittu_loitsu = input("Mitä ilmastovoimaa käytät konnia vastaan?: ").strip().lower()
            
            if valittu_loitsu not in opitut_loitsut:
                print("Et osaa tätä taikaa!")
                continue
                
            mahti = laske_luonnon_voima(valittu_loitsu, ika)
            print("\nKutsut luonnon voiman:", valittu_loitsu.upper())
            print("Loitsun kokonaismahti on:", mahti)
            
            if pelaaja.sijanti.nimi == "Salametsästäjien leiri":
                if valittu_loitsu == "kalliomurska":
                    print("[KALLIOMURSKA] Maa repeää salametsästäjien jalkojen alla! Heidän leirinsä tuhoutuu ja konnat pakenevat!")
                    tila["vartijat_voitettu"] = True
                    tila["pisteet"] += 40
                elif mahti >= 50:
                    print("Luonnonilmiö pyyhkii leirin yli! Konnat juoksevat karkuun suuren ilmastohäiriön takia.")
                    tila["vartijat_voitettu"] = True
                    tila["pisteet"] += 25
                else:
                    print("Voima oli liian heikko murtamaan konna-leiriä. Tarvitset vahvemman loitsun!")
                    
            elif pelaaja.sijanti.nimi == "Pimeä lohikäärmeen luola":
                if valittu_loitsu == "jäätävä pyörremyrsky":
                    print("[JÄÄTÄVÄ PYÖRREMYRSKY] Luola täyttyy purevasta pakkasesta ja jäisestä viimasta!")
                    print("Häkin vartijat jäätyvät kohmeeseen, pudottavat aseensa ja pakenevat luolasta lämmittelemään!")
                    tila["vartijat_voitettu"] = True
                    tila["pisteet"] += 30
                else:
                    print("Tuntematon taika tässä huoneessa.")
                    
            else:
                print("Täällä on rauhallista. Säästä luonnonvoimat sinne, missä konnat uhkaavat lohikäärmettä!")

        elif komento == "pisteet":
            nayta_pisteet(tila["pisteet"])


        elif komento == "reppu":
            pelaaja.nayta_inventaario()

        elif komento == "liiku":
            # Kolmen muuttopaikan valinta
            print("Minne haluat liikkua?")
            print("1 - Linnan pääsali (aula)")
            print("2 - Pimeä luola (luola)")
            print("3 - Salametsästäjien leiri (leiri)")
            valinta = input("Valitse numero: ")
            
            if valinta == "1":
                pelaaja.liiku(aula)
                print(huoneiden_kuvaukset[pelaaja.sijanti.nimi])
            elif valinta == "2":
                pelaaja.liiku(luola)
                print(huoneiden_kuvaukset[pelaaja.sijanti.nimi])
            elif valinta == "3":
                pelaaja.liiku(leiri)
                print(huoneiden_kuvaukset[pelaaja.sijanti.nimi])
            else:
                print("Tuntematon paikka.")
                continue

        elif komento == "pelasta":
            if pelaaja.sijanti != luola:
                print("Et voi pelastaa lohikäärmettä täältä. Sinun täytyy olla luolassa!")
                continue

            if tila["vartijat_voitettu"] == False:
                print("\nHäkin ympärillä on salametsästäjiä vartioimassa!")
                print("Et voi pelastaa lohikäärmettä suoraan. Sinun täytyy ensin käyttää luonnonvoimia")
                print("komennolla 'loitsu' ajaaksesi heidät karkuun luolasta tai heidän leiristään!")
                continue

            # Katsotaanpa, mitä tavaroita repussa on
            onko_avain = any(e.nimi == "Kulta-avain" for e in pelaaja.esineet)
            onko_miekka = any(e.nimi == "Miekka" for e in pelaaja.esineet)
            onko_pihdit = any(e.nimi == "Pihdit" for e in pelaaja.esineet)

            # --- POLKU 1: Ideaalinen (Kulta-avaimella) ---
            if onko_avain:
                print("\n========================================")
                print("KÄYTÄT KULTA-AVAINTA JA VAPAUTAT LOHIKÄÄRMEEN!")
                print("Lohikäärme lentää vapauteen ja pelastaa metsän ekosysteemin.")
                print("VOITIT PELIN! Onneksi olkoon!")
                print("========================================")
                peli_kaynnissa = False
            
            # --- POLKU 2: Voima (miekalla) ---
            elif tila["vartijat_voitettu"] == True and (onko_miekka or onko_pihdit):
                print("\n==================================================")
                print("KAS, LUONNONVOIMAT OVAT JO AJANEET VARTIJAT PAKOON!")
                print("Käytät työkaluja ja avaat suojaamattoman häkin helposti.")
                print("VOITIT PELIN (Ilmastonsuojelijan lopputulos)!")
                print("==================================================")
                peli_kaynnissa = False

            elif onko_miekka:
                isku = laske_voima(miekka.paino, ika)
                if isku > 40:
                    print("\n==============================================")
                    print("RIKOIT LUKON MIEKALLA! Lohikäärme on vapaa!")
                    print("Luonto ja ekosysteemi on pelastettu voimallasi!")
                    print("VOITIT PELIN!")
                    print("==============================================")
                    peli_kaynnissa = False
                else:
                    print("Miekka on liian painava tai voimasi ei riittänyt murtamaan lukkoa.")

            elif onko_pihdit:
                print("\nYrität katkaista kalterit pihdeillä, mutta vartija huomaa sinut!")
                vastaus = input("Mikä uhkaa eniten luontoa? (salametsästys/kierrätys): ").lower()
                
                if vastaus == "salametsästys":
                    print("\n========================================")
                    print("Vartija tajusi virheensä ja antaa sinun vapauttaa lohikäärmeen.")
                    print("Harvinainen laji on pelastettu! Ekologinen tasapaino palautettu.")
                    print("VOITIT PELIN!")
                    print("========================================")
                    peli_kaynnissa = False
                else:
                    print("Vartija huusi: 'Väärä vastaus!' ja ajoi sinut pois.")

            else:
                print("Et voi pelastaa lohikäärmettä vielä. Tarvitset Kulta-avaimen, Miekan tai Pihdit!")

        else:
            print("Tuntematon komento. Yritä uudelleen.")

if __name__ == "__main__":
    main()