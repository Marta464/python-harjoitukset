tuumat = float(input("Anna tuumat: "))

while tuumat >= 0:
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit} senttimetriä.")
    tuumat = float(input("Anna tuumat: "))
    
print("Ohjelma lopetettu.")