import random

class Player(object):
    diceLost = 0
    
    def __init__(self, name, numOfDice, diceRolls = []):
        self.name = name
        self.numOfDice = numOfDice
        self.diceRolls = diceRolls
        
    def getName(self):
        return self.name
    
    def getNumOfDice(self):
        return self.numOfDice

    def getDiceRolls(self):
        return self.diceRolls

    def getDiceLost(self):
        return self.diceLost
    
    def setName(self, name):
        self.name = name
        
    def setNumOfDice(self, num):
        self.numOfDice = num

    def setDice(self):
        self.diceRolls = []
        for x in range(self.numOfDice):
            self.diceRolls.insert(x, random.randint(1,6))

    def setDiceLost(self, num):
        self.diceLost = num
        
    def decNumOfDice(self):
        self.numOfDice -= 1

    def incDiceLost(self):
        self.diceLost += 1
        
    def _str_(self):
        return "Player: " + self.name + "\nNumber of dice: " + self.numOfDice + \
               "\nDice rolls: " + self.diceRolls + "\nNum of dice lost: " + \
               diceLost
        
