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

        DiceNumber = 5
        DiceSides = 6
        Num_of_Rolls = initiateThrows()
        Combolist = autoroll(DiceNumber, DiceSides, Num_of_Rolls)

        Bust = Combolist.count(0)
        Two = Combolist.count(1)
        TwoTwo = Combolist.count(2)
        Three = Combolist.count(3)
        Straight = Combolist.count(4)
        FullH = Combolist.count(5)
        Four = Combolist.count(6)
        Five = Combolist.count(7)
        print("You threw the Dice "+str(Num_of_Rolls)+" Times. In this you rolled nothing "+str(Bust)+" amount of times!\nYou got Two of a kind "+str(Two)+" times!\n You got "+TwoTwo+" Two pairs!\n you got Three of a kind "+Three+" Times!\n You got a straight "+Straight+" Times!\n You managed to get "+FullH+" Full Houses!\nGood job "+Four+" Four of a kinds!\n Wow, you got Five of a kind "+Five+"Times! Lucky you!\n                                   .''.       \n       .''.      .        *''*    :_\\/_:     . \n      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.\n  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-\n :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'\n : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *\n  '..'  ':::'     * /\\ *     .'/.\\'.   '\n      *            *..*         :")
