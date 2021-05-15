class Adventurer:
    #creates class for the adventurer
    def __init__( self, characterName, diveNumber, sandDollars, healthHearts ):
        self.name = characterName
        self.diveNumber = diveNumber
        self.sandDollars = sandDollars
        self.healthHearts = healthHearts
        
    def getName( self ):
        return self.name
    
    def reduceDives( self ):
        self.diveNumber = self.diveNumber - 1
        return self.diveNumber
        
    def addToSandDollars( self, newSandDollars ):
        self.sandDollars = self.sandDollars + newSandDollars
    
    def loseHealth( self ):
        self.healthHearts = self.healthHearts - 1



import random
from random import randrange

def loseHealthHearts():
    getLoseHealthHearts = random.randrange( 10, 46 )
    return getLoseHealthHearts

def collectSandDollars():
    dollarsCollected = random.randrange( 1, 6 )
    return dollarsCollected
    
def faceEnemy():
    animalFactor = random.randrange( 1, 101 )
    if animalFactor <= 33:
        return 'sharks.'
    elif animalFactor > 33 and animalFactor <= 66:
        return 'jelly fish.'
    elif animalFactor > 66 and animalFactor <= 100:
        return 'electric eels.'
    
def getDive():
    enemyFactor = random.randrange( 1, 101 )
    if enemyFactor <= 50:
        return 'Enemies'
    else:
        return 'Sand Dollars'
    

def main():
    print("You, James Ricardo, have been shipwrecked upon a small island chain in the Carribean called the Lost Keys.")
    print("The keys are inhabited by an indegenous people who have not been civilized.")
    print("They approach you and demand that you leave their sacred lands by swimming away. Yikes!")
    print("You know that this would undoubtably lead to your death, so you attempt to negotiate.")
    print(" ")
    print("The chief proceeds to offer you a deal. The indegenous people believe in a rare, magical sand dollar that when found and sacrificed brings goodwill from their gods.")
    print("They are only found in the shallows on a beach teeming with sharks, poisonious jellyfish, and electric eels.")
    print("If you can collect a satisfactory number of these rare sand dollars the cheif has agreed to relocate you by ship to a nearby civilized island.")
    print(" ")
    playGame = input("Do you accept this challenge? (y/n) ")
    
    if playGame == "y":
        print(" ")
        print("You have accepted the chief's deal. He tells you that you have up to 5 dives to the bottom of the shallows, collecting as many rare sand dollars as possible.")
        print("You will know them when you see them as they are coral blue. Normal, non-magical sand dollars are white.")
        print(" ")
        print("If you can survive the perils at hand and the chief is pleased with your results you will live.")
        print("Let's play! The chief hands you a knife to fight off the attacking beasties.")
        myAdventurer = Adventurer( "James", 5, 0, 100 )
        print("{} you have {} dives remaining, {} sand dollars and {} health hearts.".format(myAdventurer.name, myAdventurer.diveNumber, myAdventurer.sandDollars, myAdventurer.healthHearts ) )
        print("Good luck!")
        print(" ")
             
    else:
        print(" ")
        print("You did not accept the chief's deal and are forced to swim away and you drown!")
        print("GAME OVER!")
        exit()
    
    continueGame = input("Take a deep breath, it's about 15 feet to the seafloor! Are you ready to dive? (y/n) ")
    newDive = getDive()
         
    while (continueGame == "y" and myAdventurer.diveNumber >= 1 and myAdventurer.healthHearts >= 1):
        #counts down dive attempts of adventurer
        myAdventurer.diveNumber -= 1
        print(" ")
        #per dive, determines whether adventurer will be able to collect sand dollars or face enemies
        newDive = getDive()
        if newDive == 'Sand Dollars':
            getCollectSandDollars = collectSandDollars()
            print("You collected", getCollectSandDollars, "magical sand dollars. Nice job!")
            #adds to total of sand dollars collected
            myAdventurer.sandDollars = myAdventurer.sandDollars + getCollectSandDollars
            print("{} you have {} dives remaining, {} sand dollars and {} health hearts left.".format(myAdventurer.name, myAdventurer.diveNumber, myAdventurer.sandDollars, myAdventurer.healthHearts ) )
            print(" ")
            continueGame = input("If you have remaining dives and health hearts, you may dive again? (y/n) ")
        elif newDive == 'Enemies':
            faceTheEnemy = faceEnemy()
            print("You must fight off the", faceTheEnemy)
            getLoseHealthHearts = loseHealthHearts()
            print("Ouch! You lost", getLoseHealthHearts, "health hearts.")
            #subtracts health hearts from total
            myAdventurer.healthHearts = myAdventurer.healthHearts - getLoseHealthHearts            
            print("{} you have {} dives remaining, {} sand dollars and {} health hearts left.".format(myAdventurer.name, myAdventurer.diveNumber, myAdventurer.sandDollars, myAdventurer.healthHearts ) )
            print(" ")
            continueGame = input("If you have remaining dives and health hearts, you may dive again? (y/n) ")
    else:
        if myAdventurer.healthHearts >= 1 and myAdventurer.sandDollars >= 4:
            print(" ")
            print("{} you finished with {} sand dollars and {} health hearts.".format(myAdventurer.name, myAdventurer.sandDollars, myAdventurer.healthHearts ) )
            print("CONGRATULATIONS!! The chief says you collected enough magical sand dollars! He will heal any of your wounds and deliver you back to civilization!")
        else:
            print(" ")
            print("{} you finished with {} sand dollars and {} health hearts.".format(myAdventurer.name, myAdventurer.sandDollars, myAdventurer.healthHearts ) )
            print("GAME OVER! You have lost!")
    
main()
        

