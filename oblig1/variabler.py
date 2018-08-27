# To variabler med heltallsverdier
variable_1 = 2
variable_2 = 4

# Summen av de to variablene 
sum = variable_1 + variable_2

# Printer variablene på hver sin linje, og summen til slutt.
# F-strings krever Python 3.6
print(f"{variable_1}\n{variable_2}\nSum: {sum}")

# To tekstvariabler
variable_3 = "Marco"
variable_4 = "Polo"

# Legge tekstvariablene sammen
sammen = variable_3 + variable_4

# Printer tekstvariablene på hver sin linje, inkludert sammen
print(f"{variable_3}\n{variable_4}\nSammen: {sammen}")

# Lager en ny sammen-tekst med mellomrom mellom
sammen = variable_3 + " " + variable_4

# Printer den nye sammen-teksten
print(f"Sammen: {sammen}")
