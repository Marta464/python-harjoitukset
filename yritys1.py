# Luodaan lista nimeltä 'autot'
autot = [
    # Ensimmäinen auto (sanakirja)
    {
        "merkki": "Toyota",
        "malli": "Corolla",
        "vuosimalli": 2018
    },
    # Toinen auto (sanakirja)
    {
        "merkki": "Ford",
        "malli": "Focus",
        "vuosimalli": 2020
    },
    # Kolmas auto (sanakirja)
    {
        "merkki": "VW",
        "malli": "ID.3",
        "vuosimalli": 2023
    }
]

print(autot[2]["merkki"], autot[2]["malli"], autot[2]["vuosimalli"])
for sanakirja in autot:
    #print(auto["merkki']}, Malli: {sanakirja['malli']}, Vuosimalli: {sanakirja['vuosimalli']}")
    print (f"Merkki: {sanakirja['merkki']}, Malli: {sanakirja['malli']}, Vuosimalli: {sanakirja['vuosimalli']}")