from cards import *

class Player:
    def __init__(self, pName):
        self.name = pName
        self.hand = []
        self.value = 0
        self.value_type = ''
        self.winnings = 0
        self.bet = 0
        
    def checkSoftValue(self):
        self.value = 0
        # first check for aces
        # make them all 1s instead of 11s
        for card in self.hand:
            if card.value == 11:
                card.value = 1
            self.value += card.value

        # incement them back as necessary
        for card in self.hand:
            if card.value == 1:
                if self.value + 10 <= 21:
                    card.value += 10
                    self.value += 10
            
        # if there are any 11s left, set to soft
        self.value_type = 'H'
        for card in self.hand:
            if card.value == 11:
                self.value_type = 'S'

    def hitHand(self, Card1):
        self.hand.append(Card1)
        self.checkSoftValue()

    def dealHand(self, Card1, Card2):
        self.hitHand(Card1)
        self.hitHand(Card2)

    def printHand(self):
        for card in self.hand:
            print(card.deck, card.suite, card.name, card.value)
        print(self.name, "value:", self.value_type, self.value)

    def printValue(self):
        print(self.name, "value:", self.value_type, self.value)

    def printDealerUp(self):
        self.hand[0].printCard()
        print('---------------')
        
    def collectHandCards(self):
        self.value = 0
        self.value_type = ''

        while len(self.hand) != 0:
            self.hand.pop()

    def startBet(self, pBet):
        self.bet = pBet
        print(self.name, "bets", self.bet)

    def makeDoubleBet(self):
        self.bet *= 2

    def wins(self, pBet):
        self.winnings += pBet
        print(self.name, "wins", pBet)

    def loses(self, pBet):
        self.winnings -= pBet
        print(self.name, "loses", pBet)
        
    def resetBet(self):
        self.bet = 0
