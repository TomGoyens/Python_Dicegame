from Dicegame_Functions import *

init = False
play = True

while play == True:

#initialisatie
    if init == False:
        Qroll = Start()
        init = True

#Quit doublecheck:
    if Qroll == "n" or Qroll == "N":

        Qroll = QuitCheck()
        if Qroll == "y":
            play = False
        elif Qroll == "n":
            init = False

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
        print("You threw the Dice "+str(Num_of_Rolls)+" Times.\n In this you rolled nothing "+str(Bust)+" amount of times!\n You got Two of a kind "+str(Two)+" times!\n You got "+str(TwoTwo)+" Two pairs!\n you got Three of a kind "+str(Three)+" Times!\n You got a straight "+str(Straight)+" Times!\n You managed to get "+str(FullH)+" Full Houses!\n Good job "+str(Four)+" Four of a kinds!\n Wow, you got Five of a kind "+str(Five)+" Times! Lucky you!\n                                   .''.       \n       .''.      .        *''*    :_\\/_:     . \n      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.\n  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-\n :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'\n : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *\n  '..'  ':::'     * /\\ *     .'/.\\'.   '\n      *            *..*         :")

        Qroll = PlayAgain()
