#1. Er dette lovlig kode? Begrunn svaret.
# Nei. Det som gjør koden ulovlig er print-setningen. Det hadde gått fint om b hadde vært en string, men den er gjort om til int og da kan den ikke settes sammen så enkelt med +-operatoren.
# Ellers er det pent om man holder seg til én stil, og her sløyfer mellomrommet mellom print og parentesene ettersom metodene over ikke har et slikt mellomrom.

#2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
# Først og fremst det som er nevnt i 1. punkt over. I tillegg er det en if-setning uten elif eller else. 
# Dette er ikke et umiddelbart problem, men ettersom du sjekker for én tilstand, burde det være en reaksjon i fravær av den forventede verdien (som her er 10).

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")

