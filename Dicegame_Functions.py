import random
#import math

#asks user input for a 'yes' or 'no' anwser
def yorn(Question):
    while True:
        Qroll = input(Question +" (y/n): ")
        print ("")
        if Qroll == "y"or Qroll == "Y":
            return "y"
        elif Qroll == "n"or Qroll == "N":
            return "n"
        else:
            print ("please enter either 'y' or 'n'  (or 'Y'/'N')")
            print ("")

def Start():
    Question = "Wanna play?"
    return yorn(Question)

def PlayAgain():
    Question = "Play again?"
    return yorn(Question)

def QuitCheck():
    Question = "Are you sure you want to quit?"
    return yorn(Question)

#asks user for input on the gamemode. currently available are free dice throwing and Poker Dice
def Gamemode():
    while True:
        mode = input ("select your gamemode. ('0' for free custom dice rolling, '1' for poker dice): ")
        print ("")
        if int(mode)==0 or int(mode)==1:
            mode = int(mode)
            return mode
        print ("please enter a valid character.")
        print ("")

def AskNum(Question, Min):
    init = False
    while init == False:
        tally = 0
        Number = input("Please enter the number of "+str(Question)+".: ")
        print ("")
        for character in Number:
            if character  not in "0123456789":
                tally += 1
        if tally > 0 or int(Number) < Min:
            print ("Please enter an integer (at least '"+str(Min)+"').")
            print ("")
        else:
            init = True
    Number = int(Number)
    return Number

#function to get number of dice
def initiateDice():
    Question = "Dice"
    Min = 1
    return AskNum(Question, Min)

#function to get number sides of the dice
def initiateDiceSides():
    Question = "Sides of the Dice"
    Min = 3
    return AskNum(Question, Min)

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

def sum(list):
    sum = 0
    for i in range (len(list)):
        sum += list[i]
    return sum

def Pokerify(DiceRoll, DiceNumber):
    for i in range(DiceNumber):
        if DiceRoll[i] == 1:
            DiceRoll[i] = "9"
        elif DiceRoll[i] == 2:
            DiceRoll[i] = "10"
        elif DiceRoll[i] == 3:
            DiceRoll[i] = "J"
        elif DiceRoll[i] == 4:
            DiceRoll[i] = "Q"
        elif DiceRoll[i] == 5:
            DiceRoll[i] = "K"
        else:
            DiceRoll[i] = "A"
    return DiceRoll

def PokerScore(DiceDupes):
    DiceDupesSorted = sorted(DiceDupes, reverse=True)
    if DiceDupesSorted[0] == 5:
        Score = "Five of a kind!"
    elif DiceDupesSorted[0] == 4:
        Score = "Four of a kind!"
    elif DiceDupesSorted[0] == 3 and DiceDupesSorted[1] == 2:
        Score = "Full house!"
    elif DiceDupesSorted[4] != 0 and DiceDupes[0] == 0:
        Score = "It's a straight!"
    elif DiceDupesSorted[0] == 3:
        Score = "Three of a kind!"
    elif DiceDupesSorted[0] == 2:
        if DiceDupesSorted[1] == 2:
            Score = "Two pair!"
        else:
            Score = "Two of a kind!"
    else:
        Score = "It's a bust!"
    return Score

#def Pokerify2(DiceDupes, DiceNumber):
