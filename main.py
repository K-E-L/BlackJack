from cards import *
from players import *
from game import *


def main():
    # game.testPlayOne()
    # game.testBasic()

#    systems = ["Hi Lo", "Wong Halves", "Uston SS", "Revere APC", "Uston APC", "Victor APC"]
    systems = ["Hi Lo"]

    # play one game for each system and append to file
    for system in systems:
        game = Game(pSystem=system, pDeckCount=2, pCardsCut=15, pSpread=20, pBetDuringNegativeCount=1)
        game.play()
        game.printStats()
        game.fileStats()
        
    # # play only one game and append to file
    # game = Game("Hi Lo", 2, 15, 20, 0)
    # game.play()
    # game.printStats()
    # game.fileStats()

    # # test game
    # game = Game("Hi Lo", 2, 15, 20, 0)
    # game.testPlayOne()

    # # test game
    # game = Game("Hi Lo", 2, 15, 20, 0)
    # game.testBasic()
    
        
if __name__  == "__main__":
    main()
