# Izračunati povprečno oceno vseh študentov. OK
# Najti študenta z najvišjo oceno.
# Izpisati imena študentov, ki imajo oceno nad 85.

studenti = [
    {"ime": "Oseba1", "ocena": 2},
    {"ime": "Oseba2", "ocena": 2},
    {"ime": "Oseba3", "ocena": 4},
    {"ime": "Oseba4", "ocena": 5},
    {"ime": "Oseba5", "ocena": 5},
    {"ime": "Oseba6", "ocena": 5},
    {"ime": "Oseba7", "ocena": 4},
    {"ime": "Oseba8", "ocena": 3},
    {"ime": "Oseba9", "ocena": 1},
    {"ime": "Oseba10", "ocena": 2},
    {"ime": "Oseba11", "ocena": 1},
]

steviloOseb = 11
povprecjeOcen = 0

for povprecje in studenti:
    povprecjeOcen += povprecje["ocena"]
    skupnoPovprecje = povprecjeOcen / steviloOseb
print(f"Povprečje ocen med študenti = {skupnoPovprecje:.1f}")

najvisjaOcena = studenti[0]
for najvisja in studenti:
    if najvisja["ocena"] > najvisjaOcena["ocena"]:
        najvisjaOcena = najvisja
print(f"Najvisjo oceno ima {najvisjaOcena["ime"]} in sicer {najvisjaOcena["ocena"]}.")

for povprecje in studenti:
    if povprecje["ocena"] > 3:
        print(f"Studentje ki presegajo oceno 3 so: {povprecje["ime"]} in ima oceno {povprecje["ocena"]}.")

