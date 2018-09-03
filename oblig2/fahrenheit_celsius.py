# Prosedyre som gjør om fahrenheit til celsius
def f_to_c(fahrenheit):
    c = (fahrenheit - 32) * (5/9)
    return c

# Tar inn grader Fahrenheit, gjør den om til float og lagrer den
F = float(input("F = "))

# Finner grader Celsius og printer
C = f_to_c(F)
print("C = %.2f" % C)
