import random
import string
def password():

    Wachtwoord = []
    Lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z"]
    Uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nummerlijst = ["1","2","3","4","5","6","7","8","9","0"]
    special = ["@","#","$","%","&","_","?"]
    woordlengte = 6



    for i in range (woordlengte):
        LowerCaseAlfabet = random.choice(Lowercase)
        Wachtwoord += LowerCaseAlfabet

        CapsLockAlfabet = random.choice(Uppercase)
        Wachtwoord += CapsLockAlfabet
        
        NummerList = random.choice(nummerlijst)
        Wachtwoord += NummerList
        
        Specialtekens = random.choice(special)
        Wachtwoord += Specialtekens
    
        



    random.shuffle(Wachtwoord)
    random.shuffle(Wachtwoord)

    WachtwoordCode = "".join(Wachtwoord)
    print (WachtwoordCode)
    return WachtwoordCode

password()


