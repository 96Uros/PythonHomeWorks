

osebje = [
   {"ime": "Jure", "placa": 1500, "delavnoMesto": "proizvodnja"},
   {"ime": "Spela", "placa": 1900, "delavnoMesto": "uprava"},
   {"ime": "Maks", "placa": 1400, "delavnoMesto": "montaza"},
   {"ime": "Alen", "placa": 2000, "delavnoMesto": "IT"},
   {"ime": "Tone", "placa": 4500, "delavnoMesto": "CEO"}
]

print("Zaposleni delavci v podjetju;")
for imena in osebje:
    print(f"Moje ime je {imena["ime"]} in opravljam delavno mesto {imena["delavnoMesto"]}")

skupnaPlaca = 0
for zaposleni in osebje:
    skupnaPlaca += zaposleni["placa"]

steviloZaposlenih = 5
povprecnaPlaca = skupnaPlaca / steviloZaposlenih
print(f"|Povprečna plača v podjetju je {povprecnaPlaca} €|")