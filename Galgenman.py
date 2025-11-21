import random
from the_List import *


Word = random.choice(list)

wordLengths = len(Word)
Leben = wordLengths


print ('Wilkommen zum Spiel')

while Leben > 0:
    print ( "Du hast ", Leben, " Leben")
    print("Geben sie ein Buchstaben ein")
    Zeichen = str(input())
    Leben = Leben - 1


print ("Du hast Versagt. Das Wort ist:" + Word)