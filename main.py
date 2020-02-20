from spillebrett import Spillebrett

def main():
    print("for å lage en generasjon trenger jeg to tall, \n m(rader) og n(kolonner) som skal være dimensjonene\n")
    rader = int(input("vennligst tast inn ant rader\n"))
    kolonner = int(input("vennligst tast inn ant kolonner\n"))
    brett = Spillebrett(rader, kolonner)
    print("nå kommer nulte generasjon av brettet\n \n")
    brett.tegnBrett()
    terminal = "e"
    while True:
        print("dette er en menyløkke.")
        print("hvis du ønsker å fortsette å simulere brettet, tast mellomrom")
        print("hvis du ønsker å gi deg, tast q\n")
        terminal = input("hva er ditt valg?")
        if(terminal=="q"):
            break
        brett.oppdatering()
        brett.tegnBrett()
#Starte hovedprogrammet
main()
