from cards import *

class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.value_type = ''
        self.winnings = 0
        self.bet = 0
        
    def checkSoftValue(self):
        self.value = 0
        check = False
        # first check for aces
        # make them all 1s instead of 11s
        for card in self.hand:
            if card.value == 1:
                check = True
            elif card.value == 11:
                check = True
                card.value = 1
            self.value += card.value

        # return hard value
        if check == False:
            self.value_type = 'H'
            return

        # incement them back as necessary
        for card in self.hand:
            if card.value == 1:
                if self.value + 10 <= 21:
                    card.value += 10
                    self.value += 10
            
        # if there are any 1s left, set to hard
        self.value_type = 'S'
        for card in self.hand:
            if card.value == 1:
                self.value_type = 'H'
                
    def dealHand(self, Card1, Card2):
        self.hand.append(Card1)
        self.hand.append(Card2)

        self.checkSoftValue()

    def hitHand(self, Card1):
        self.hand.append(Card1)
        self.checkSoftValue()

    def printHand(self, user_name):
        for card in self.hand:
            print(card.deck, card.suite, card.name, card.value)
        print(user_name, "value:", self.value_type, self.value)

    def printValue(self, user_name):
        print(user_name, "value:", self.value_type, self.value)

    def printDealerUp(self):
        print(self.hand[0].deck, self.hand[0].suite, self.hand[0].name, self.hand[0].value)
        
    def collectHandCards(self):
        self.value = 0
        self.value_type = ''

        while len(self.hand) != 0:
            self.hand.pop()

    def setBet(self, pBet):
        self.winnings -= pBet
        self.bet = pBet
