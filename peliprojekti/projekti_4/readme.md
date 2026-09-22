# Matin Seikkailu — Peliprojekti

Tämä on Pythonilla toteutettu tekstipohjainen seikkailupeli. Ohjelma yhdistää kurssin **Projekti 4 (Ohjelman rakenne ja oliot)** sekä **Projekti 5 (Tiedostonkäsittely)** vaatimukset samaan toimivaan kokonaisuuteen.

## Ohjelman rakenne (Projekti 4)
Peli on jaettu selkeisiin moduuleihin olio-ohjelmoinnin periaatteiden mukaisesti:
- `main.py`: Pelin pääohjelma ja ohjaussilmukka (päävalikko).
- `pelaaja.py`: `Pelaaja`-luokka, joka hallitsee pelaajan nimeä, sijaintia, inventaariota ja liikkumista.
- `huone.py`: `Huone`-luokka, joka määrittää pelimaailman huoneet ja niissä olevat esineet.
- `esine.py`: `Esine`-luokka, joka määrittää pelissä kerättävät tavarat (esim. Kulta-avain, Miekka) ja niiden painot.

## Tiedostonkäsittely (Projekti 5)
Projektissa 5 peliä on laajennettu seuraavilla tiedostonkäsittelyominaisuuksilla:
1. **Ohjeet ja intro**: Pelin käynnistyessä esittelyteksti luetaan tiedostosta `intro.txt` ja peliohjeet tiedostosta `ohjet.txt`.
2. **Pelin tallennus**: Kun pelaaja antaa komennon `lopeta`, pelitilanne (pelaajan nimi, nykyinen sijainti ja kerätyt esineet) tallennetaan automaattisesti tiedostoon `tallenna.txt`.
3. **Pelin lataus**: Käynnistyksen yhteydessä ohjelma tarkistaa, onko vanhaa tallennusta olemassa. Jos on, pelaaja voi jatkaa peliä suoraan siitä, mihin hän jäi.

**Tekijä:** Marta