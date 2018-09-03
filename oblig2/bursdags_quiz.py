# Dette er en quiz hvor du skal gjette bursdagen til programmereren.
# Gjettingen foregår med tall. Gjetter du feil får du tilbakemelding og må kjøre programmet på nytt.

print("Gjett bursdagen min! Først måned, så dag. Gjøres med tall")

month = int(input("Gjett hvilken måned det er i? "))

if month <= 0:
    print("Hallo, året har jo måneder da! Du klarer bedre.")
elif month > 0 and month <= 3:
    print("Dessverre, det er senere på året.")
elif month == 4 or month == 6:
    print("Du er veldig nærme!")
elif month == 5:
    print("Stemmer, mai er helt riktig!")

    day = int(input("Nå, hvilken dag er det? "))

    if day <= 0:
        print("Det er vel ikke et helt realistisk tall, eller?!")
    elif day > 0 and day <= 6:
        print("Det er litt senere.")
    elif day == 7:
        print("TJOHO, bra jobba! 7. mai er årets beste dag <B-)")
    elif day > 7 and day <= 31:
        print("Det er tidligere.")
    else:
        print("Jeg vet ikke hvor du har informasjonen din fra, men så mange dager har ikke mai.")

elif month > 6 and month <= 12:
    print("Godt gjetta, men det er tidligere på året enn det!")
else:
    print("Ah, din tullebukk!")
