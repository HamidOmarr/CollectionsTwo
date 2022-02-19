import random
lootjes = []
deelnemervraag = int(input("Met hoeveel willen jullie deelnemen?"))
while deelnemervraag:
    for x in range (deelnemervraag):
        naamvraag = input("Wat is jouw naam?")
        if naamvraag in lootjes:
            print ("Zelfde naam, probeer het weer opnieuw!")
            deelnemervraag = deelnemervraag + 1
        else:
            lootjes.append(naamvraag)

    for x in range (len(lootjes)):
        if lootjes[x] == random.choice(lootjes):
            print("Probeer het weer opnieuw.")
        else:
            print (lootjes[x],"heeft:",random.choice(lootjes),"Geloot!")
    break  

            

             
