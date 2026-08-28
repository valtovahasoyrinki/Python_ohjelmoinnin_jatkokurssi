kaikki = ""

while True:
    syote = input("Kerro nimi")
    if syote == "lopeta":
        break
    kaikki = kaikki + syote + "\n"
print("Tulos on:")
print(kaikki)

