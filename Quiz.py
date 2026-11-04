import random as rand
Antal_rätt = 0
antal_frågor = 0
i = 3
a = 1
b = 3
c = 0

while True:
    ordning = rand.randint(a, b)
    if ordning == 1:
        print("1.  Oslo")
        print("2.  Stockholm")
        print("3.  Köpenhamn")
        Svar = int(input("Vilken är Sveriges huvudstad?"))
        print("Ditt val: ",Svar)
        antal_frågor += 1
        if Svar == 2:
            print("Rätt!")
            Antal_rätt += 1
        else:
            print("Fel!")
        a = a + 1

    elif ordning == 2 and c == 0:
        print("1.  Oslo")
        print("2.  Stockholm")
        print("3.  Köpenhamn")
        Svar_2 = int(input("Vilken är Norges huvudstad?"))
        print("Ditt val: ",Svar_2)
        antal_frågor += 1
        if Svar_2 == 1:
           print("Rätt!")
           Antal_rätt += 1
        else:
            print("Fel!")
        c = c + 1

    elif ordning == 3:
        print("1.  Atlanten")
        print("2.  Indiska oceanen")
        print("3.  Stilla havet")
        Svar_3 = int(input("Vad heter världens största hav?"))
        if Svar_3 == 3:
           print("Rätt!")
           Antal_rätt += 1
        else:
            print("Fel!")
        b = b - 1

print("Du fick", Antal_rätt, "av", antal_frågor, "rätt.")