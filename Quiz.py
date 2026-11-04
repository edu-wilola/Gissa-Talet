Antal_rätt = 0
antal_frågor = 0
Svar = input("Vilken är Sveriges huvudstad?")
print("1.  Oslo")
print("2.  Stockholm")
print("3.  Köpen")
print("Ditt val: ",Svar)
antal_frågor += 1
if Svar == 2:
    print("Rätt!")
    Antal_rätt += 1
else:
    print("Fel!")

Svar_2 = input("Vilken är Sveriges huvudstad?")
print("1.  Oslo")
print("2.  Stockholm")
print("3.  Köpen")
print("Ditt val: ",Svar_2)
antal_frågor += 1
if Svar == 2:
    print("Rätt!")
    Antal_rätt += 1
else:
    print("Fel!")
print("Du fick", Antal_rätt, "av", antal_frågor, "rätt.")