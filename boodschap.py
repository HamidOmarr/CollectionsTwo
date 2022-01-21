lijst = []
while True:
    SupermarktItem = input("wat voor item wil je toevoegen")
    SupermarktTotaal= int(input("hoeveel wil je van deze item"))
    lijst.append(SupermarktItem)
    lijst.append(SupermarktTotaal)
    verdergaan = input("wil je verdergaan?")
    if verdergaan == "N":
        break

print (lijst)


