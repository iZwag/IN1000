from hund import Hund

def hovedprogram():
    hund = Hund(vekt=15, alder=10)
    hund.spring()
    hund.print_vekt()
    hund.spring()
    hund.print_vekt()
    hund.spring()
    hund.print_vekt()
    hund.spring()
    hund.print_vekt()
    hund.spis(1)
    hund.print_vekt()
    hund.spis(4)
    hund.print_vekt()

hovedprogram()
