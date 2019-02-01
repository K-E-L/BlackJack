import sys

class BettingSystem:
    def __init__(self):
        self.running_count = 0
        self.min_running_count = 0
        self.max_running_count = 0
        self.true_count = 0
        self.min_true_count = 0
        self.max_true_count = 0

        # max experimental true count
        self.exp_max_true_count = 35

        # 
        
        self.total_true_count = 0

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

    def updateTrueCount(self, pDecksLeftInShoe):
        self.true_count = round(self.running_count / pDecksLeftInShoe)

    def updateTotalTrueCount(self):
        self.total_true_count += self.true_count

    def setExpMaxTrueCount(self, pExpMaxTrueCount):
        self.exp_max_true_count = 35

    def getExpMaxTrueCount(self):
        return self.exp_max_true_count

    def getTrueCount(self):
        return self.true_count
    

class HiLo(BettingSystem):
    def updateRunningCount(self, pCards):
        card = pCards[len(pCards) - 1]
        if card.value >= 2 and card.value <= 6:
            self.running_count += 1
        elif card.value == 10 or card.value == 1:
            self.running_count -= 1

class WongHalves(BettingSystem):
    def updateRunningCount(self, pCards):
        card = pCards[len(pCards) - 1]
        if card.value == 1 or card.value == 10:
            self.running_count -= 1
        elif card.value == 9:
            self.running_count -= .5
        elif card.value == 2 or card.value == 7:
            self.running_count += .5
        elif card.value == 3 or card.value == 4 or card.value == 6:
            self.running_count += 1
        elif card.value == 5:
            self.running_count += 1.5
