from errno import EILSEQ

kaikki = ""

while True:
    syote = input("Kerro nimi")
    if syote == "lopeta":
        break
    kaikki = kaikki + syote + "\n"
print("Tulos on:")
print(kaikki)

while True:
    nimi = input("kerro nimi")
    if nimi == "lopeta":
        break
    elif nimi == "kake":
        continue
    else:
        print(f"Terve {nimi}!")



