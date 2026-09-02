syote = input("Anna luku (tyhjä lopettaa): ")


pienin = None
suurin = None


while syote != "":
    
    luku = float(syote)
    
    
    if pienin is None and suurin is None:
        pienin = luku
        suurin = luku
    else:

        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
            
    syote = input("Anna luku (tyhjä lopettaa): ")

if pienin is not None:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")