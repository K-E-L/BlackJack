from cards import *
from players import *
from basic import *

class Game:
    def __init__(self):
        self.shoe = Shoe()
        self.dealer = Player()
        self.user = Player()

        self.dealer_wins = 0
        self.user_wins = 0

        # self.games = int(input("Enter how many games to play: "))
        self.games = 50

    def calculateBet(self, pWon):
        if pWon == 1:
            self.user.winnings += (self.user.bet * 2)
        elif pWon == -1:
            self.dealer.winnings += self.user.bet
        else:
            self.user.winnings += self.user.bet
            
    # just plays war for now..
    def calculateGame(self, value1, value2):
        if value1 > value2:
            self.dealer_wins += 1
            return 1
            # print("dealer won")
        elif value1 == value2:
            return 0
        else:
            self.user_wins += 1
            # print("user won")
            return -1

    def play(self):
        while(self.games > 0):
            self.games -= 1
            # bet here
            self.user.setBet(1)
            
            #deal hands out
            self.dealer.dealHand(self.shoe.dealCard(), self.shoe.dealCard())
            self.user.dealHand(self.shoe.dealCard(), self.shoe.dealCard())

            self.dealer.printDealerUp()
            self.user.printHand("user")

            # play basic strategy
            choice = playBasic(self.user, self.dealer, self.shoe)
            
            # calculate who wins /
            won = self.calculateGame(self.dealer.value, self.user.value)

            # update who wins the bet
            self.calculateBet(won)

            # clean up user hands
            self.dealer.collectHandCards()
            self.user.collectHandCards()

            
    
    def printStats(self):
        print("user wins:", self.user_wins)
        print("dealer wins:", self.dealer_wins)
        # print("ratio", self.user_wins / self.dealer_wins)
        print("user winnings", self.user.winnings)
        print("dealer winnings", self.dealer.winnings)
