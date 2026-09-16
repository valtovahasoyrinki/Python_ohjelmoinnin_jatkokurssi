kurssit = [{"nimi" : "matikka", "pisteet" : 10, "arvosana" : 5},
           {"nimi" : "fysiikka", "pisteet" : 5, "arvosana" : 3}]
def pisteSumma(kurssilista: list):
    pisteet = 0
    for kurssi in kurssilista:
        pisteet = pisteet+kurssi["pisteet"]
    return pisteet

print(pisteSumma(kurssit))

def keskiarvo(kurssilista):
    arvosanat = 0
    for kurssi in kurssilista:
        arvosanat += kurssi["arvosana"]
    return arvosanat/len(kurssilista)

print(keskiarvo(kurssit))

def p_keskiarvo(kurssilista):
    p_arvosanat = 0
    pisteet = 0
    for kurssi in kurssilista:
        p_arvosanat += kurssi["arvosana"]   * kurssi["pisteet"]
        pisteet += kurssi["pisteet"]

    return p_arvosanat/pisteet

print(p_keskiarvo(kurssit))

def tulostakurssit(kurssit):
    for kurssi in kurssit:
        print(kurssit)
        return

tulostakurssit(kurssit)