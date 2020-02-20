class Celle:
    
    #Konstruktør
    def __init__(self):
        self.status = False
        self.nord = None
        self.sor = None
        self.vest = None
        self.ost = None
        self.nordvest = None
        self.nordost = None
        self.sorvest = None
        self.sorost = None
        self.naboer = [self.nord, self.sor, self.vest, self.ost, self.nordvest, self.nordost, self.sorvest, self.sorost]

    #Endre status
    def settDoed(self):
        self.status = False

    def settLevende(self):
        self.status = True

    #Hente status
    def erLevende(self):
        return self.status

    def hentNaboArray(self):
        aktiveNaboer = []
        for l in self.naboer:
            if(l!=None):
                aktiveNaboer.append(l)
            else:
                print("tomt")
        return aktiveNaboer

    def hentStatusTegn(self):
        if self.status:
            return "O"
        else:
            return "."