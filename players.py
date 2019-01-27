from cards import *

class Player:
    def __init__(self, pName):
        self.name = pName
        self.hand = []
        self.value = 0
        self.value_type = ''
        self.winnings = 0
        self.bet = 0
        self.max_bet = 0
        # spread of 50
        self.spread = 50
        self.total_bet = 0

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

    def updateMaxBet(self):
        if self.bet > self.max_bet:
            self.max_bet = self.bet

    def updateTotalBet(self):
        self.total_bet += self.bet
            
    def startBet(self, pBet):
        self.bet = pBet
        self.updateMaxBet()
        self.updateTotalBet()
        print(self.name, "bets", self.bet)

    def forceMapToSpread(self, pShoe):
        # bet / (experimental max bet) == spread bet / (max spread value)
        # spread bet == (max spread value) * bet / (experimental max bet)

        pShoe.exp_max_true_count = 35
        self.bet = round((self.spread * self.bet) / pShoe.exp_max_true_count)

        if self.bet <= 0:
            self.bet = 1

    # from WIRED https://www.youtube.com/watch?v=G_So72lFNIU
    def hiLowBet(self, pShoe):
        self.bet = pShoe.true_count - 1
        
        if self.bet <= 0:
            self.bet = 1
        else:
            self.forceMapToSpread(pShoe)
            if self.bet > self.spread:
                self.bet = self.spread

        print(self.name, "Hi-Low spread bets", self.bet)
        self.updateMaxBet()
        self.updateTotalBet()


    def hiLowBetModified(self, pTrueCount):
        self.bet = pTrueCount
        self.updateMaxBet()
        if self.bet <= 0:
            self.bet = 1
        print(self.name, "Hi-Low bets", self.bet)
        
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
