from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self.genNr = 0
        self.brett = []
        for i in range(rader):
            rad = []
            for j in range(kolonner):
                nyCelle = Celle()
                rad.append(nyCelle)
            self.brett.append(rad)
        self._generer()
        #self.opprettPekere()

        #for i in range(rader):
            #for j in range(kolonner):
                #print(self.brett[i][j].hentStatusTegn())

    def tegnBrett(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self.brett[i][j].hentStatusTegn(), end="")
            print("\n")
        print("dette er generasjon: "+ str(self.genNr))

    def oppdatering(self):
        #Selve oppdateringen
        #self.genNr+=1
        nyeLevende = []
        nyeDode = []
        for i in range(self._rader):
            for j in range(self._kolonner):
                #hent array med naboer,
                #loop og separer i dode og levende
                celleNaboer = self.finnNabo(i, j)
                #print(len(celleNaboer))
                #print("lengden til cellenabo over")
                levende = 0
                if(self.brett[i][j].status):
                    for h in celleNaboer:
                        if(h.status):
                            levende = levende +1
                    if levende>3 or levende<2:
                        nyeDode.append(self.brett[i][j])
                elif(self.brett[i][j].status==False):
                    for g in celleNaboer:
                        if(g.status):
                            levende+=1
                    if levende==3:
                        nyeLevende.append(self.brett[i][j])
        for r in nyeLevende:
            r.settLevende()
        for t in nyeDode:
            t.settDoed()
        self.genNr+=1


    def finnAntallLevende(self):
        antallLevende = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self.brett[i][j].status:
                    antallLevende+=1
        return antallLevende


    def _generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                if randint(1,3)==3:
                    self.brett[i][j].settLevende()

 
    def finnNabo(self, rad, kolonne):
        #midl = self.brett[rad][kolonne].hentNaboArray()
        #print(len(midl))
        #print("lengden til midl")
        #vanlig tilfelle:
        print("inne i finnNabo")
        l=[]
        if (0<rad<self._rader-1) and (0<kolonne<self._kolonner-1):
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad][kolonne-1])
            l.append(self.brett[rad+1][kolonne+1])
            l.append(self.brett[rad+1][kolonne-1])
            l.append(self.brett[rad-1][kolonne+1])
            l.append(self.brett[rad-1][kolonne-1])
            print("standard")
            print(len(l))
        
        #øvre rad
        elif rad==0 and (0<kolonne<self._kolonner-1):
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad+1][kolonne+1])
            l.append(self.brett[rad+1][kolonne-1])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad][kolonne-1])
        #nedre rad
        elif rad==self._rader-1 and (0<kolonne<self._kolonner-1):
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad-1][kolonne+1])
            l.append(self.brett[rad-1][kolonne-1])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad][kolonne-1])
        #venstre side
        elif (0<rad<self._rader-1) and kolonne==0:
            print(rad)
            print("ok")
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad+1][kolonne+1])
            l.append(self.brett[rad-1][kolonne+1])
        #høyre side
        elif (0<rad<self._rader-1) and kolonne==self._kolonner-1:
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad][kolonne-1])
            l.append(self.brett[rad+1][kolonne-1])
            l.append(self.brett[rad-1][kolonne-1])
        #øvre venstre
        elif rad==0 and kolonne==0:
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad+1][kolonne+1])
            print("øvre venstre")
            print(len(l))
        #nedre venstre
        elif rad==self._rader-1 and kolonne==0:
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad][kolonne+1])
            l.append(self.brett[rad-1][kolonne+1])
            print("nedre venstre")
            print(len(l))
        #øvre høyre
        elif rad==0 and kolonne==self._kolonner-1:
            l.append(self.brett[rad+1][kolonne])
            l.append(self.brett[rad][kolonne-1])
            l.append(self.brett[rad+1][kolonne-1])
            print("øvre høyre")
            print(len(l))
        #nedre høyre
        elif rad==self._rader-1 and kolonne==self._kolonner-1:
            l.append(self.brett[rad-1][kolonne])
            l.append(self.brett[rad][kolonne-1])
            l.append(self.brett[rad-1][kolonne-1])
            print("nedre høyre")
            print(len(l))
        return l