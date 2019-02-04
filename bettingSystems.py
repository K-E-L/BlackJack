class BettingSystem:
    def __init__(self):
        self.running_count = 0
        self.min_running_count = 0
        self.max_running_count = 0
        self.true_count = 0
        self.min_true_count = 0
        self.max_true_count = 0
        self.total_true_count = 0

        # max experimental true count
        self.exp_max_true_count = 30

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

    def getExpMaxTrueCount(self):
        return self.exp_max_true_count

    def getTrueCount(self):
        return self.true_count

    def updateRunningCount(self, pCards):
        card = pCards[len(pCards) - 1]
        self.running_count += self.count_table[card.value - 1]

        
class HiLo(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Hi Lo"
        # for values       [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.count_table = [-1, 1, 1, 1, 1, 1, 0, 0, 0, -1]

class WongHalves(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Wong Halves"
        # for values       [ 1,  2,  3,  4,   5,  6,  7,  8,   9,  10]
        self.count_table = [-1, .5,  1,  1, 1.5,  1, .5,  0, -.5, -1]

class UstonSS(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Uston SS"
        # for values       [ 1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.count_table = [-2, 2, 2, 2, 3, 2, 1, 0, -1, -2]

class RevereAPC(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Revere APC"
        # for values       [ 1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.count_table = [-4, 2, 3, 3, 4, 3, 2, 0, -1, -3]
        
class UstonAPC(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Uston APC"
        # for values       [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.count_table = [0, 1, 2, 2, 3, 2, 2, 1, -1, -3]

class VictorAPC(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Victor APC"
        # for values       [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.count_table = [0, 2, 2, 2, 3, 2, 2, 0, -1, -3]

# ------ not included in main -----------------
        
class AdvancedOmega2(BettingSystem):
    def __init__(self):
        BettingSystem.__init__(self)
        self.name = "Advanced Omega 2"
        # for values       [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.count_table = [0, 1, 1, 2, 2, 2, 1, 0, -1, -2]

# ---------------------------------------------
