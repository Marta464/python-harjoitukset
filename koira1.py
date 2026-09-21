class koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuf - vuf"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print (self.nimi + "hakkuu" + self.haukahdus)
        return   
