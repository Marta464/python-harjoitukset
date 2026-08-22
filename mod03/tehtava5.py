leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luoti_grammoina = luoti * 13.3
naula_grammoina = naula * 32 * 13.3
leiviska_grammoina = leiviska * 20 * 32 * 13.3

yhteisgrammat = luoti_grammoina + naula_grammoina + leiviska_grammoina

kilogrammat = int(yhteisgrammat // 1000)
grammat = yhteisgrammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
