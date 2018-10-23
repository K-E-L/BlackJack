from cards import *
from players import *

class Game:
    def __init__(self):
        self.shoe = Shoe()
        self.garbage = Garbage()
        self.dealer = Player()
        self.user = Player()

        self.dealer_wins = 0
        self.user_wins = 0

        self.shoe.shuffleCards()
        
    # just plays war for now..
    def calculate(self, value1, value2):
        if value1 > value2:
            self.dealer_wins += 1
            # print("dealer won")
        else:
            self.user_wins += 1
            # print("user won")

    def play(self):
        # loop through one shoe
        while(not self.shoe.isEmpty()):
            #deal hands out
            self.dealer.dealHand(self.shoe.dealCard(), self.shoe.dealCard())
            self.user.dealHand(self.shoe.dealCard(), self.shoe.dealCard())
            
            # self.dealer.printHand("dealer")
            # self.user.printHand("self.user")

            # calculate who wins
            self.calculate(self.dealer.value, self.user.value)

            # later.. add betting before you deal hands
            # later.. add basic strategy before calculate
            # later.. add to calculate to include who wins money

            # clean up user hands
            self.garbage.addCard(self.dealer.collectHandCard())
            self.garbage.addCard(self.dealer.collectHandCard())
            self.garbage.addCard(self.user.collectHandCard())
            self.garbage.addCard(self.user.collectHandCard())
    
    def printStats(self):
        print("user wins:", self.user_wins)
        print("dealer wins:", self.dealer_wins)
        print("ratio", self.user_wins / self.dealer_wins)
