import urllib.request
import json

pyynto = urllib.request.urlopen("https://users.metropolia.fi/~peterh/kurssit.json")

data = pyynto.read()

kurssit = json.loads(data)

print(len(kurssit))
print(f"Kurssit ennen lisäystä: {kurssit}")

uusi_kurssi = {"nimi": "mina ja koirani", "pisteet" : 4, "arvosana" : 5 }
kurssit.append(uusi_kurssi)

kurssit1 = json.dumps(kurssit)

print(f"Kurssit lisäyksen jälkeen: {kurssit1}")

with open ("kurssit.json", "w") as outfile:
    data = json.dumps(kurssit)
    outfile.write(data)

print(data)