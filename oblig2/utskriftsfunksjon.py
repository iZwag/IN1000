# Lag prosedyre ut av første deloppgave
def navn_og_sted():
    # Tar inn et navn
    navn = input("Skriv inn navn: ")
    
    # Tar inn bosted
    bosted = input("Hvor kommer du fra? ")
    
    # Hilser på personen og minner dem på hvor de er fra
    print("Hei, {}! Du er fra {}".format(navn, bosted))

# Kjører prosedyren 3 ganger
for i in range(0,3):
    navn_og_sted()
