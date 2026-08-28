# Tehtävä 1 opintolaskuri
# Nimi: Valto Vähäsöyrinki
# Opiskelijanumero: 2520408


kurssitulostus = ""
kurssien_määrä = 0
pisteiden_summa = 0
arvosanojen_summa = 0
painotettu_summa = 0

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

    kurssien_määrä = kurssien_määrä + 1
    pisteiden_summa = pisteiden_summa + opintopisteet
    arvosanojen_summa = arvosanojen_summa + arvosana
    painotettu_summa = painotettu_summa + arvosana * opintopisteet

    kurssitulostus = kurssitulostus + f"{kurssien_määrä}. {nimi}({opintopisteet}op): {arvosana}\n"


print("Opintopisteet yhteensä", pisteiden_summa)

if kurssien_määrä > 0:
    print("Suoritetut kurssit:")
    print(kurssitulostus, end="")

    keskiarvo = arvosanojen_summa / kurssien_määrä
    painotettu_keskiarvo = painotettu_summa / pisteiden_summa

    print(f"Arvosanojen keskiarvo: {keskiarvo}")
    print(f"Arvosanojen painotettu keskiarvo: {painotettu_keskiarvo}")
