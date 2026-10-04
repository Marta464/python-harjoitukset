nopeus = int(input(f"Anna nopeus: "))
rajoitus = int(input("Anna nopeusrajoitus: "))

if nopeus <= 20:
    print("Aajat sallittua nopeutta.")
elif nopeus > rajoitus + 20:
    print("Sakkoraja ylittyi!")
else:
    print("Ajat ylinopeutta.")

print(f"Auton nopeus oli {nopeus} km/h.")