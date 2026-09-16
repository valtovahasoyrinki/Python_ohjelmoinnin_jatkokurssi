# Tehtävä 2 opintoarvosanalaskuri
# Nimi: Valto Vähäsöyrinki
# Opiskelijanumero: 2520408

import csv
with open('t4.csv', 'r') as csvfile:
    lukija = csv.reader(csvfile, delimiter=',')
    for rivi in lukija:
        name = rivi[0]
        price = rivi[1]
        print(f"name", name)
        print(f"price", price)
