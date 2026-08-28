nimilista = []

while True:
    syote = input("No?")
    if syote == "lopeta":
        break
    nimilista.append(syote)

nimilista.sort()

print(nimilista)