from itertools import combinations
import random
kaartendeck = []   
kaartenkleur = ['Harten','Klaveren','Schoppen','Ruiten']
kaarten13 = ['2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas','Joker','Joker']
for kleur in kaartenkleur:
   for kaart in kaarten13:
        combinatie = kleur + " " + kaart
        kaartendeck.append(combinatie)

for x in range(1,8):
    for kleur in kaartenkleur:
        for kaart in kaarten13:
            Randomkaartendeck  = random.choice(kaartendeck)
    print (Randomkaartendeck)
print (kaartendeck)

  