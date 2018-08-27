# Stiller brukeren et spørsmål og lagrer svaret
svar = input("Kunne du tenke deg en brus? \"ja\"/\"nei\" + ENTER ")

# Sjekker svaret og gir korrekt tilbakemelding
if svar == "ja":
    print("Her har du en brus!")
elif svar == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")

