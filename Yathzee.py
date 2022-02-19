import random

TotaalOpslag = []
totaal = []
punten = 0
ronde = 1
pogingen = 3
dobbelsteen = [1,2,3,4,5,6]


while pogingen > 0: 
    print ("ronde:", ronde)
    print ("poging:", pogingen)
    print ("Punten:", punten)
    for x in range(1,6):
        totaal.append(random.choice(dobbelsteen))
    print (totaal)
    Nogeenkeer = input("Wil je nog een keer gooien? (3 kansen)")
    if Nogeenkeer == "J":
        for x in range (len(totaal)):
            OpslagRol = input(print("zou jij", totaal[x] ,"willen houden?"))
            if OpslagRol == "J":
                TotaalOpslag.append(totaal[x])
        print (str(TotaalOpslag))
        if '3' in TotaalOpslag:
            punten += 1
            
        pogingen = pogingen - 1
        totaal.clear()
  
    if Nogeenkeer == "N" or pogingen <= 0: 
        pogingen = 3 
        ronde = ronde + 1
        TotaalOpslag.clear()
        totaal.clear()


        
        
