def gallonat_litroiksi(gallonat):
    """Muuntaa Yhdysvaltain nestegallonat litroiksi."""
    return gallonat * 3.785

while True:
    syote = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))
    
    if syote < 0:
        print("Bensiinin määrä ei voi olla negatiivinen. Lopetetaan.")
        break 

litrat = gallonat_litroiksi(syote)
print(f"{syote} gallonaa on {litrat:.3f} litraa.")