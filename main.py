import randint
spelaren_namn = input("Vad heter du?")
print("Hej", spelaren_namn, "och välkommen till spelet!")

rätt_tal = randint(1,11)
tal = int(input("Gissa ett tal mellan 1 och 10:"))
if tal != rätt_tal:
    print("Tyvärr, det var 3")
elif tal == rätt_tal:
    print("Snyggt jobbat!")
