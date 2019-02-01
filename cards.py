import random
from bettingSystems import *

class Card:
    def __init__(self, deck, suite, name, value):
        self.deck = deck
        self.suite = suite
        self.name = name
        self.value = value

    def printCard(self):
        print(self.deck, self.suite, self.name, self.value)

class Shoe:    
    def __init__(self):
        self.cards = []

        # self.deck_count = int(input("Enter how many decks are in the shoe: "))
        # playing with a 6 deck shoe
        self.deck_count = 6
        # self.deck_count = 2
        
        # cut one deck out
        self.cards_cut = 52
        # self.cards_cut = 15

        # deck estimation of .5 means round to half deck, 0 means don't round
        self.deck_estimation = 0
        
        # self.system = HiLo()
        self.system = WongHalves()
        
        self.setShoe()
        self.shuffleCards()

    def setShoe(self):
        for numSuite in range(4):
            if (numSuite == 0):
                tempSuite = 'C'
            if (numSuite == 1):
                tempSuite = 'S'
            if (numSuite == 2):
                tempSuite = 'D'
            if (numSuite == 3):
                tempSuite = 'H'
            for numVal in range(13):
                for numDeck in range(self.deck_count):
                    if (numVal) < 1:
                        card = Card(numDeck, tempSuite, 'A', numVal+1)
                    elif (numVal) == 10:
                        card = Card(numDeck, tempSuite, 'J', 10)
                    elif (numVal) == 11:
                        card = Card(numDeck, tempSuite, 'Q', 10)
                    elif (numVal) == 12:
                        card = Card(numDeck, tempSuite, 'K', 10)
                    else:
                        card = Card(numDeck, tempSuite, numVal+1, numVal+1)
                    self.cards.append(card)

    def createCard(self, pValue):
        return Card(0, '?', '?', pValue)

    def printCards(self):
        for card in self.cards:
            print(card.deck, card.suite, card.name, card.value)

    def shuffleCards(self):
        random.shuffle(self.cards)
            
    def decksLeftInShoe(self, pDeckEstimation):
        cards_left = len(self.cards)
        if pDeckEstimation != 0: 
            rounded = round((cards_left / 52) * (1/pDeckEstimation)) / (1/pDeckEstimation)
            if rounded == 0:
                rounded = pDeckEstimation
            # print("rounded---------------------", rounded)
        else:
            rounded = cards_left / 52
            # print("rounded---------------------", rounded)
            
        return rounded
    
    def dealCard(self):
        # should only happen if cards cut is 0
        if len(self.cards) == 0:
            print("Shoe is out.. creating and shuffling new shoe")
            self.setShoe()
            self.shuffleCards()
            self.system.running_count = 0
            

            self.system.updateRunningCount(self.cards)
            self.system.updateTrueCount(self.decksLeftInShoe(self.deck_estimation))
            self.system.updateMinMaxRunningCount()
            self.system.updateMinMaxTrueCount()
            self.system.updateTotalTrueCount()
            return self.cards.pop()
        else:
            self.system.updateRunningCount(self.cards)
            self.system.updateTrueCount(self.decksLeftInShoe(self.deck_estimation))
            self.system.updateMinMaxRunningCount()
            self.system.updateMinMaxTrueCount()
            self.system.updateTotalTrueCount()
            return self.cards.pop()

    def isEmpty(self):
        if not self.cards:
            return True

    def checkCutForShuffle(self):
        if len(self.cards) <= self.cards_cut:
            print("Shoe is less than or equal to cut.. creating and shuffling new shoe")
            self.setShoe()
            self.shuffleCards()
            self.system.running_count = 0
            self.system.true_count = 0
        else:
            # print("cards left:", len(self.cards))
            pass

