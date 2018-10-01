# Først defineres funksjonen, minFunksjon(), som ikke tar noen parametere. 
# Deretter defineres funksjonen, hovedprogram(), som heller ikke tar noen parametere. 
# Så kalles hovedprogram. 
# I hovedprogram settes først a til 42, så b til 0. 
# Deretter printes b til terminalen, som altså vil vise kun "0".
# Så settes b til a, som gjør at både b og a nå er 42.
# Så settes a lik returverdien av minFunksjon, som nå kalles.
# I minFunksjon startes en for-løkke med iterasjonsvariabel x som iterer blindt 2 ganger, gitt av range(2).
# Inne i for-løkken settes først c til 2.
# Så printes c, hvorledes det nå står "2" i terminalen.
# Så inkrementeres c med 1, så nå er c = 3.
# Deretter settes b til 10.
# Deretter legges a til verdien til b, men a er ikke definert i miljøet til minFunksjon, så her blir det en feilmelding.
# - Det vil si, selvom a er definert i hovedprogram, så skjer det totalt lukket og kan ikke sees av minFunksjon.
# FEILMELDING OG AVSLUTTET PROGRAM
# Resten er ting som ville skjedd om a hadde blitt ansett som 0 i steden for udefinert:
# b printes, da står det "10".
# Løkken kjøres igjen, c settes til 2, c printes igjen "2", c inkrementeres til 3.
# b settes til 10 igjen, prøver å legge til a, det funker ikke, b ville vært "10".
# Så returneres b. 
# Tilbake i hovedprogram blir a nå altså 10, returnert fra minFunksjon.
# b printes til "42".
# a printes til "10".
# Og så er programmet ferdig.

# Under limes programmet inn for gjennomkjøring etter at denne flytenbeskrivelsen er ferdig.

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
