from cards import *

class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.value_type = ''

    def checkSoftValue(self):
        # check for S or H
        temp_value_type = 'H'
        for card in self.hand:
            if(card.value == 1):
                temp_value_type = 'S'
                card.value += 10
        self.value_type = temp_value_type

        # update value
        for card in self.hand:
            self.value += card.value
    
    def dealHand(self, Card1, Card2):
        self.hand.append(Card1)
        self.hand.append(Card2)

        self.checkSoftValue()

    def printHand(self, user_name):
        for card in self.hand:
            print(card.deck, card.suite, card.name, card.value)
        print(user_name, "value:", self.value_type, self.value)

    def collectHandCard(self):
        self.value = 0
        self.value_type = ''
        return self.hand.pop()
