import random
import string
def password():

    Wachtwoord = []
    woordlength = random.randrange(24)

    for i in range(woordlength):
        LowerCaseAlfabet = random.choice(string.ascii_lowercase)
        Wachtwoord += LowerCaseAlfabet

        CapsLockAlfabet = random.choice(string.ascii_uppercase)
        Wachtwoord += CapsLockAlfabet

        NummerList = random.choice(string.digits)
        Wachtwoord += NummerList
        
        Specialtekens = random.choice(string.punctuation)
        Wachtwoord += Specialtekens
        
        



    random.shuffle(Wachtwoord)
    random.shuffle(Wachtwoord)

    WachtwoordCode = "".join(Wachtwoord)
    print (WachtwoordCode)
    return WachtwoordCode

password()


