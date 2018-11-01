from Dicegame_Functions import *

init = 0
initDice = 0

while True:

#initialisatie
    if init == 0:
        Qroll = initialise()
        init = 1

#Quit doublecheck:
    if Qroll == "n" or Qroll == "N":

        Qroll = QuitCheck()
        if Qroll == "y":
            break
        elif Qroll == "n":
            init = 0

#playing the 'game'
    elif Qroll == "y" or Qroll == "Y":

        if initDice == 0:
            Mode = Gamemode()
            if Mode == 0:
                DiceNumber = initiateDice()
                DiceSides = initiateDiceSides()
            elif Mode == 1:
                DiceNumber = 5
                DiceSides = 6
            initDice = 1

        DiceRoll = roll(DiceNumber, DiceSides) #rolls the dice and saves the roll
        DiceDupes = dupelist(DiceRoll, DiceNumber, DiceSides)#list of the number of times a number has been rolled
        if Mode == 1:
            DiceRoll = Pokerify(DiceRoll, DiceNumber)
            Score = PokerScore(DiceDupes)
        print ("your Diceroll is:" + str(DiceRoll))
        print ("")
        if Mode == 1:
            print(Score)
            print ("")
#        print ("Number of times you got a number(in order):" + str(DiceDupes))

        Qroll = PlayAgain()
