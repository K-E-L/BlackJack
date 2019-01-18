import random

class Card:
    def __init__(self, deck, suite, name, value):
        self.deck = deck
        self.suite = suite
        self.name = name
        self.value = value

    def printCard(self):
        print(self.deck, self.suite, self.name, self.value)

class Shoe:
    deck_count = 0
    cards = []

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
    
    def __init__(self):
        # self.deck_count = int(input("Enter how many decks are in the shoe: "))
        
        # playing with a 2 deck shoe
        self.deck_count = 2
        self.setShoe()
        self.shuffleCards()

    def createCard(self, pValue):
        return Card(0, '?', '?', pValue)

    def printCards(self):
        for card in self.cards:
            print(card.deck, card.suite, card.name, card.value)

    def shuffleCards(self):
        random.shuffle(self.cards)

    def dealCard(self):
        if len(self.cards) == 0:
            print("Shoe is out.. creating and shuffling new shoe")
            self.setShoe()
            self.shuffleCards()
            return self.cards.pop()
        else:
            return self.cards.pop()

    def isEmpty(self):
        if not self.cards:
            return True
