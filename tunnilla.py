class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koirat = []
svuosi = 2016
nimi = "Iriska"
for i in range(10):

    koirat.append(Koira(nimi, svuosi))
    svuosi += 1
    nimi = chr(ord(nimi) + 1)
for koira in koirat:
    print(koira.nimi) 

koira1 = Koira(nimi="Iriska", syntymävuosi=2016)