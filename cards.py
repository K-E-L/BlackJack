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
    running_count = 0
    min_running_count = 0
    max_running_count = 0
    true_count = 0
    min_true_count = 0
    max_true_count = 0

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

    def updateRunningCount(self):
        card = self.cards[len(self.cards) - 1]
        if card.value >= 2 and card.value <= 6:
            self.running_count += 1
        elif card.value == 10 or card.value == 1:
            self.running_count -= 1

    def updateMinMaxRunningCount(self):
        if self.running_count > self.max_running_count:
            self.max_running_count = self.running_count
        elif self.running_count < self.min_running_count:
            self.min_running_count = self.running_count

    def updateMinMaxTrueCount(self):
        if self.true_count > self.max_true_count:
            self.max_true_count = self.true_count
        elif self.true_count < self.min_true_count:
            self.min_true_count = self.true_count
            
    def decksLeftInShoe(self):
        cards_left = len(self.cards) 
        rounded = round((cards_left / 52) * 2) / 2
        if rounded == 0:
            rounded = .5

        return rounded
    
    def updateTrueCount(self):
        self.true_count = round(self.running_count / self.decksLeftInShoe())

    def dealCard(self):
        if len(self.cards) == 0:
            print("Shoe is out.. creating and shuffling new shoe")
            self.setShoe()
            self.shuffleCards()
            self.updateMinMaxRunningCount()
            self.updateMinMaxTrueCount()
            self.running_count = 0
            self.updateRunningCount()
            self.updateTrueCount()
            return self.cards.pop()
        else:
            self.updateRunningCount()
            self.updateTrueCount()
            self.updateMinMaxRunningCount()
            self.updateMinMaxTrueCount()
            return self.cards.pop()

    def isEmpty(self):
        if not self.cards:
            return True

