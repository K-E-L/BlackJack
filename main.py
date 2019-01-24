from cards import *
from players import *
from game import *

def main():
    game = Game()

    # game.testPlayOne()
    
    # game.testBasic()

    game.play()
    game.printStats()
    
if __name__  == "__main__":
    main()
