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
        Mode = input ("select your gamemode. ('0' for free custom dice rolling, '1' for poker dice): ")
        print ("")
        if Mode == "0" or Mode == "1" or Mode == "2":
            Mode = int(Mode)
            return Mode
        print ("please enter a valid character.")
        print ("")

#function to ask user to input an integer higher than a certian minimum
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

#function to get number of dicethrows
def initiateThrows():
    Question = "times you want to throw the dice"
    Min = 1
    return AskNum(Question, Min)

#roll funtion generates random numbers between 1 and 6 for number of dice given
def roll(DiceNumber, DiceSides):
    DiceRoll = [0]*DiceNumber
    for i in range(DiceNumber):
        #DiceRoll[i] = math.ceil(random.random()*6) #math.ceil(random.random()*6) kan vervangen worden door random.randint(1,6)
        DiceRoll[i] = random.randint(1,DiceSides)
    return DiceRoll

#dupecheck function checks the number of duplicates for number given
def Dupecheck(number,DiceRoll, DiceNumber):
    tally = 0
    for i in range(DiceNumber):
        if number == DiceRoll[i]:
            tally += 1
    return tally

#dupelist makes a list of possible duplicates (for each number possible)
def Dupelist(DiceRoll,DiceNumber, DiceSides):
    DiceDupes = [0]*DiceSides
    for i in range(DiceSides):
        DiceDupes[i] = Dupecheck(i+1,DiceRoll, DiceNumber)
    return DiceDupes

#function to change the diceroll to it's Poker dice counterpart
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

#function to check the score of the (poker)diceroll
#def PokerScore(DiceDupes):
#    DiceDupesSorted = sorted(DiceDupes, reverse=True)
#    if DiceDupesSorted[0] == 5:
#        Score = "Five of a kind!\n                                   .''.       \n       .''.      .        *''*    :_\\/_:     . \n      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.\n  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-\n :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'\n : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *\n  '..'  ':::'     * /\\ *     .'/.\\'.   '\n      *            *..*         :"
#    elif DiceDupesSorted[0] == 4:
#        Score = "Four of a kind!"
#    elif DiceDupesSorted[0] == 3 and DiceDupesSorted[1] == 2:
#        Score = "Full house!"
#    elif DiceDupesSorted[4] != 0 and DiceDupes[0] == 0:
#        Score = "It's a straight!"
#    elif DiceDupesSorted[0] == 3:
#        Score = "Three of a kind!"
#    elif DiceDupesSorted[0] == 2:
#        if DiceDupesSorted[1] == 2:
#            Score = "Two pair!"
#        else:
#            Score = "Two of a kind!"
#    else:
#        Score = "It's a bust!"
#    return Score

def ComboDetect(DiceDupes):
    DiceDupesSorted = sorted(DiceDupes, reverse=True)
    if DiceDupesSorted[0] == 5:
        Combo = 7
    elif DiceDupesSorted[0] == 4:
        Combo = 6
    elif DiceDupesSorted[0] == 3 and DiceDupesSorted[1] == 2:
        Combo = 5
    elif DiceDupesSorted[4] != 0 and DiceDupes[0] == 0:
        Combo = 4
    elif DiceDupesSorted[0] == 3:
        Combo = 3
    elif DiceDupesSorted[0] == 2:
        if DiceDupesSorted[1] == 2:
            Combo = 2
        else:
            Combo = 1
    else:
        Combo = 0
    return Combo

def PokerScore(Combo):
    Scorelist = ["It's a bust!","Two of a kind!","Two pair!","Three of a kind!","It's a straight!","Full house!","Four of a kind!","Five of a kind!\n                                   .''.       \n       .''.      .        *''*    :_\\/_:     . \n      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.\n  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-\n :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'\n : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *\n  '..'  ':::'     * /\\ *     .'/.\\'.   '\n      *            *..*         :"]
    return Scorelist[Combo]

#function that rolls the dice a certain number of times and saves the scores of all the rolls in a list
def autoroll(DiceNumber, DiceSides, Num_of_Rolls):
    ComboList = []
    for i in range(Num_of_Rolls):
        ComboList.append(ComboDetect(Dupelist(roll(DiceNumber, DiceSides),DiceNumber, DiceSides)))
    return ComboList
