import Dicegame_Functions.py

init = 0
initDice = 0

while True:

#initialisatie
    if init == 0:
        Qroll = Initialisatie()
        init = 1

#Quit doublecheck:
    if Qroll == "n" or Qroll == "N":

        Qroll = QuitCheck()
        if Qroll == "y":
            break
        elif Qroll == "n" or "N":
            init = 0

#playing the 'game'
    elif Qroll == "y" or Qroll == "Y":

        if initDice == 0:
            DiceNumber = initiateDice()
            DiceNumber = int(DiceNumber)
            initDice = 1

        DiceRoll = roll(DiceNumber) #rolls the dice and saves the roll
        DiceDupes = dupelist(DiceRoll, DiceNumber)

        print ("your Diceroll is:" + str(DiceRoll))
        print ("Number of times you got a number(in order):" + str(DiceDupes))

        Qroll = input("Play again? (y/n)")

    else:
        print ("please enter either 'y' or 'n'  (or 'Y'/'N')")
        init = 0
