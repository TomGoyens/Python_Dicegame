import random
#import math

#ik weet niet 100% of deze functie juist is benaamd
def Initialisatie():
    Qroll = input("Wanna play? (y/n): ")
    return Qroll


#Quit doublecheck:
def QuitCheck():

    Qroll = input("Are you sure? (y/n): ")

    if Qroll == "y"or Qroll == "Y":
        return "y"
    elif Qroll == "n"or Qroll == "N":
        return Qroll
    else:
        print ("please enter either 'y' or 'n'  (or 'Y'/'N')")

#function to get number of dice
def initiateDice():
    initDice = 0
    while initDice == 0:
        tally = 0
        DiceNumber = input("Please enter the number of Dice.: ") #gets number of dice to be rolled and keeps asking until you give a damn integer!
        for character in DiceNumber:
            if character  not in "0123456789":
                tally += 1
        if tally > 0 or int(DiceNumber) == 0:
            print ("Please enter an integer (greater than '0').")
        else:
            initDice = 1

    DiceNumber = int(DiceNumber)
    return DiceNumber

def initiateDiceSides():
    initSide = 0
    while initSide == 0:
        tally = 0
        DiceSides = input("Please enter the number of sides of the Dice.: ") #gets number of sides of the dice to be rolled and keeps asking until you give a damn integer!
        for character in DiceSides:
            if character  not in "0123456789":
                tally += 1
        if tally > 0 or int(DiceSides) == 0 or int(DiceSides) == 1 or int(DiceSides) == 2:
            print ("Please enter an integer (minimun is '3').")
        else:
            initSide = 1

    DiceSides = int(DiceSides)
    return DiceSides

#roll funtion generates random numbers between 1 and 6 for number of dice given
def roll(DiceNumber, DiceSides):
    DiceRoll = [0]*DiceNumber
    for i in range(DiceNumber):
        #DiceRoll[i] = math.ceil(random.random()*6) #math.ceil(random.random()*6) kan vervangen worden door random.randint(1,6)
        DiceRoll[i] = random.randint(1,DiceSides)
    return DiceRoll

#dupecheck function checks the number of duplicates for number given
def dupecheck(number,DiceRoll, DiceNumber):
    tally = 0
    for i in range(DiceNumber):
        if number == DiceRoll[i]:
            tally += 1
    return tally

#dupelist makes a list of possible duplicates (for each number possible)
def dupelist(DiceRoll,DiceNumber, DiceSides):
    DiceDupes = [0]*DiceSides
    for i in range(DiceSides):
        DiceDupes[i] = dupecheck(i+1,DiceRoll, DiceNumber)
    return DiceDupes

#def PointsCalc(DiceDupes, DIceSides):
#    for i in range(DiceSides):
#        if DiceDupes[i]==
