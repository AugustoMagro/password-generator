import os
import random

class PassGenerator(object):
    """docstring for ."""

    def __init__(self):
        self.password = ""
        self.listK = []
        super().__init__()
        resp = PassGenerator.generatePass(self)
        input(f"Password gerado -> {resp}")

    def countPass(self, psw):
        self.normalChar = 0
        self.specialChar = 0
        self.number = 0
        self.capsChar = 0
        for x in range(0, len(psw)):
            ascii = ord(psw[x])
            if ascii >= 65 and ascii <= 90:
                self.capsChar += 1
            elif ascii >= 97 and ascii <= 122:
                self.normalChar += 1
            elif ascii >= 48 and ascii <= 57:
                self.number += 1
            elif ascii >= 35 and ascii <= 38 or ascii == 33:
                self.specialChar += 1

    def checkPass(self, psw):
        minSpecialChar = int(len(psw) * 0.2)
        minNumber = int(len(psw) * 0.2)
        minCapsChar = int(len(psw) * 0.1)
        if len(psw) < 10:
            print("Minimun of 10 Characteres")
            return "Fraco"

        if int(self.specialChar) >= minSpecialChar and int(self.number) >= minNumber and int(self.capsChar) >= minCapsChar:
            return "Forte"
        else:
            return "Fraco"

    def checkMinLengh(self, psw):
        minSpecialChar = int(len(psw) * 0.2)
        minNumber = int(len(psw) * 0.2)
        minCapsChar = int(len(psw) * 0.1)
        return minSpecialChar, minNumber, minCapsChar

    def generatePass(self):

        numbersChars = [x for x in range(48, 58)]
        capsChars = [ x for x in range(65, 91)]
        specialChars = [x for x in range(35, 39)]
        specialChars.append(33)
        normalChars = [ x for x in range(97, 123)]

        for x in range(0, random.choice([x for x in range(10, 20)])):
            self.password = self.password + chr(random.choice(normalChars))

        minimuns = PassGenerator.checkMinLengh(self, self.password)
        for x in range(0, minimuns[0]):
            PassGenerator.putString(self, specialChars)

        for x in range(0, minimuns[1]):
            PassGenerator.putString(self, capsChars)

        for x in range(0, minimuns[2]):
            PassGenerator.putString(self, numbersChars)

        PassGenerator.countPass(self, self.password)
        check = PassGenerator.checkPass(self, self.password)
        if check == "Fraco":
            PassGenerator()
        else:
            return self.password


    def putString(self, listChar):
        k = random.choice([x for x in range(0, len(self.password))])
        j = random.choice(listChar)
        if k in self.listK:
           PassGenerator.putString(self, listChar)
        else:
            self.password = self.password.replace(self.password[k], chr(j))
            self.listK.append(k)
            return self.password


PassGenerator()
