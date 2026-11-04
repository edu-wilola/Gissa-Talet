import randint
spelaren_namn = input("Vad heter du?")
print("Hej", spelaren_namn, "och välkommen till spelet!")

rätt_tal = randint(1,11)
i = 1
print("Gissa ett tal mellan 1 och 10")
while i <= 4:
    tal = int(input("Försök", i,": Gissa talet:"))

    if tal != rätt_tal:
        print("Fel gissat.")
        i += 1
    elif tal == rätt_tal:
        print("Rätt gissat!")
        break
    if tal > 4:
        print("Du förlorar!")
        break
