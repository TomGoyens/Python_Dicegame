from Dicegame_Functions import *

init = False
initDice = False

while True:

#initialisatie
    if init == False:
        Qroll = Start()
        init = True

#Quit doublecheck:
    if Qroll == "n" or Qroll == "N":

        Qroll = QuitCheck()
        if Qroll == "y":
            play == False
        elif Qroll == "n":
            init = 0

#playing the 'game'
    elif Qroll == "y" or Qroll == "Y":

#Decide the gamemode. (can only be done once)
        if initDice == False:
            Mode = Gamemode()
            if Mode == 0:
                DiceNumber = initiateDice()
                DiceSides = initiateDiceSides()
            elif Mode == 1:
                DiceNumber = 5
                DiceSides = 6
            initDice = True
#secret 'cheat mode'
        if Mode == 2:
            DiceRoll = [6,6,6,6,6]
            DiceDupes = [0,0,0,0,0,5]
            DiceNumber = 5
        else:# roll the dice!
            DiceRoll = roll(DiceNumber, DiceSides) #rolls the dice and saves the roll
            DiceDupes = Dupelist(DiceRoll,DiceNumber, DiceSides)#saves the amount of times a side has been rolled in a list
#the pokerdice need to be scored!
        if Mode == 1 or Mode == 2:
            DiceRoll = Pokerify(DiceRoll, DiceNumber)
            Score = PokerScore(DiceDupes)

#print the results
        print ("your Diceroll is:" + str(DiceRoll))
        print (DiceDupes)
        print ("")
        if Mode == 1 or Mode == 2:
            print(Score)
            print ("")

        Qroll = PlayAgain()
