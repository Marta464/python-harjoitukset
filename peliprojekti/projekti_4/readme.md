# Lauren Luolasto (D&D-tekstipeli)
**Kirjoittaja:** Marta Netreba

### Pelin idea ja tavoite
Tämä on fantasiatekstiseikkailu. Pelaaja löytää itsensä linnan pääsalista ja hänen on pelastettava viimeinen Smaragdilohikäärme, joka on lukittuna Pimeään luolaan.

Pelin tavoitteena on löytää Kulta-avain (Kultainen avain) "pelaa"-komennolla, tarkistaa luola "liiku"-komennolla ja käyttää lohikäärmeen "tallenta"-komentoa.

### Pitkän aikavälin kehitys (kestävä kehitys)
Peli hyödyntää YK:n työryhmää nro 15 (Maanpäällinen elämä ). Lohikäärme on harvinainen ja uhanalainen laji, joka ylläpitää luonnon ja metsäelämän tasapainoa. Pelastamalla sen salametsästäjiltä pelaaja suojelee planeetan biologista monimuotoisuutta.

### Projektin rakenne
- `main.py` — pelin pääsilmukka, valikko ja komentojen käsittely.
- `pelaaja.py` — pelaajaluokka, heidän työkalunsa ja sijaintinsa. - `huone.py` — pelin sijaintiluokka.
- `esine.py` — esineluokka ja sen paino.
- `intro.txt` ja `ohjet.txt` — tarinan teksti ja säännöt.