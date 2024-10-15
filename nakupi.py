# Izračunati skupni znesek vseh nakupov.
# Najti nakup z najvišjim zneskom.
# Izpisati nakupe, ki presegajo določen znesek (npr. 100 €).

nakupi = [
    {"Stranka": "Spela", "znesek": 120},
    {"Stranka": "Ana", "znesek": 410},
    {"Stranka": "Viktor", "znesek": 80},
    {"Stranka": "Maks", "znesek": 21},
    {"Stranka": "Mila", "znesek": 4},
    {"Stranka": "Kris", "znesek": 700},
    {"Stranka": "Joze", "znesek": 988},
    {"Stranka": "Franc", "znesek": 455},
    {"Stranka": "Marjan", "znesek": 122},
    {"Stranka": "Petra", "znesek": 99}
]

skupniZnesek = 0
for skupni in nakupi:
    skupniZnesek += skupni["znesek"]
print(f"Skupni znesek znaša {skupniZnesek} €")

najvisjiNakup = nakupi[0]
for nakup in nakupi:
    if nakup["znesek"] > najvisjiNakup["znesek"]:
        najvisjiNakup = nakup
print(f"Najvisji nakup je opravil/a {najvisjiNakup["Stranka"]} in sicer porabil je {najvisjiNakup["znesek"]} €")

for nakup in nakupi:
    if nakup["znesek"] > 100:
        print(f"Znesek 100€ presega {nakup["znesek"]} € od osebe {nakup["Stranka"]}")