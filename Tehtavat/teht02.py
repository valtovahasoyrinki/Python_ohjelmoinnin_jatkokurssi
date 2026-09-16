# Tehtävä 2 opintoarvosanalaskuri
# Nimi: Valto Vähäsöyrinki
# Opiskelijanumero: 2520408

def pisteiden_summa(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa = summa + kurssi["opintopisteet"]
    return summa


def keskiarvo(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa = summa + kurssi["arvosana"]
    return summa / len(kurssit)


def painotettu_keskiarvo(kurssit):
    summa = 0
    for kurssi in kurssit:
        summa = summa + kurssi["arvosana"] * kurssi["opintopisteet"]
    return summa / pisteiden_summa(kurssit)


def tulosta_kurssit(kurssit):
    print("Suoritetut kurssit:")
    i = 1
    for kurssi in kurssit:
        print(f"{i}. {kurssi['nimi']}({kurssi['opintopisteet']}op): {kurssi['arvosana']}")
        i = i + 1


kurssit = []

while True:
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi = input("Nimi: ")

    if nimi == "lopeta":
        break

    opintopisteet = int(input("Opintopisteet: "))

    if opintopisteet < 0 or opintopisteet > 20:
        print("Virheellinen syöte.")
        continue

    arvosana = int(input("Arvosana: "))

    if arvosana < 1 or arvosana > 5:
        print("Virheellinen syöte.")
        continue

    kurssi = {"nimi": nimi, "opintopisteet": opintopisteet, "arvosana": arvosana}
    kurssit.append(kurssi)


print("Opintopisteet yhteensä", pisteiden_summa(kurssit))

if len(kurssit) > 0:
    tulosta_kurssit(kurssit)
    print(f"Arvosanojen keskiarvo: {keskiarvo(kurssit):.1f}")
    print(f"Arvosanojen painotettu keskiarvo: {painotettu_keskiarvo(kurssit):.1f}")
