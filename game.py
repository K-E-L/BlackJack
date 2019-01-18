from cards import *
from players import *
from basic import *
from test import *

class Game:
    def __init__(self):
        self.shoe = Shoe()
        self.dealer = Player('dealer')
        self.user = Player('user')

        self.dealer_wins = 0
        self.user_wins = 0

        # self.games_init = int(input("Enter how many games to play: "))
        self.games_init = 50
        self.games_left = 0
        self.black_jacks = 0
        self.surrenders = 0

    def checkNondependent(self, pChoice):
        if pChoice == 'Bj':
            print("user blackjack!")
            # blackjack pays 3 to 2
            self.dealer.loses(1.5 * self.user.bet)
            self.user.wins(1.5 * self.user.bet)
            self.user_wins += 1
            self.black_jacks += 1
            return 1
        if pChoice == 'Su':
            print("user surrenders")
            self.dealer.wins(.5 * self.user.bet)
            self.user.loses(.5 * self.user.bet)
            self.dealer_wins += 1
            self.surrenders += 1
            return 1
        if pChoice == 'Bu':
            print("user busted, dealer won")
            self.dealer.wins(self.user.bet)
            self.user.loses(self.user.bet)
            self.dealer_wins += 1
            return 1
        else:
            return 0

    def checkDependent(self, pChoice, pDealer_Bust):

        # does not calculate bets with H and S 21 as a push
        
        self.dealer.printHand()

        if pDealer_Bust:
            print('dealer busted')
            # print('choice', pChoice)
            
        if pChoice == 'D':
            self.user.makeDoubleBet()
            if pDealer_Bust == 1 or self.user.value > self.dealer.value:
                print("user doubles, and wins")
                self.dealer.loses(self.user.bet)
                self.user.wins(self.user.bet)
                self.user_wins += 1
            elif self.user.value < self.dealer.value:
                print("user doubles, and loses")
                self.dealer.wins(self.user.bet)
                self.user.loses(self.user.bet)
                self.dealer_wins += 1
            elif self.user.value == self.dealer.value:
                print("user doubles, and pushes")

        # don't know why we need 'H' here
        elif pChoice == 'S' or pChoice == 'H':
            if pDealer_Bust == 1 or self.user.value > self.dealer.value:
                print("user stands, and wins")
                self.dealer.loses(self.user.bet)
                self.user.wins(self.user.bet)
                self.user_wins += 1
            elif self.user.value < self.dealer.value:
                print("user stands, and loses")
                self.dealer.wins(self.user.bet)
                self.user.loses(self.user.bet)
                self.dealer_wins += 1
            elif self.user.value == self.dealer.value:
                print("user stands, and pushes")

    def testPlayOne(self):
        # bet here
        self.user.startBet(1)

        value = int(input("User first card value: "))
        value1 = int(input("User second card value: "))
        value2 = int(input("Dealer first card value: "))
        value3 = int(input("Dealer second card value: "))
        #deal hands out
        self.user.dealHand(self.shoe.createCard(value), self.shoe.createCard(value1))
        self.dealer.dealHand(self.shoe.createCard(value2), self.shoe.createCard(value3))

        self.dealer.printDealerUp()
        self.dealer.printValue()
        # self.user.printHand()

        # play basic strategy
        choice = playBasic(self.user, self.dealer, self.shoe)
        self.user.printHand()

        dealer_bust = 0
        if choice == 'Sp':
            self.user.makeDoubleBet()
            card_hold = self.user.hand.pop()
            choice = playSplit(self.user, self.dealer, self.shoe)
            self.user.printHand()
            result = self.checkNondependent(choice)
            if not result:
                dealer_bust = playDealer(self.dealer, self.shoe)
                self.checkDependent(choice, dealer_bust)
            self.user.collectHandCards()
            choice = playSplit1(self.user, self.dealer, self.shoe, card_hold)
            self.user.printHand()
            result = self.checkNondependent(choice)
            if not result:
                self.checkDependent(choice, dealer_bust)

        else:
            # calculate who wins / update bet
            result = self.checkNondependent(choice)
            if not result:
                dealer_bust = playDealer(self.dealer, self.shoe)
                self.checkDependent(choice, dealer_bust)

    def testSplits(self):
        basicDict = {}
        makeSplitDict(basicDict)
        for value in range(1, 11):
            for value1 in range(1, 11):
                # value = int(input("User first card value: "))
                # value1 = int(input("User second card value: "))
                # value2 = int(input("Dealer first card value: "))
                #deal hands out
                self.user.dealHand(self.shoe.createCard(value), self.shoe.createCard(value))
                self.dealer.dealHand(self.shoe.createCard(value1), self.shoe.createCard(2))

                # play basic strategy
                choice = playTestBasic(self.user, self.dealer, self.shoe)
                answer = basicDict[(value1, value, value)]
                if (choice == answer):
                    # print(value1, '--', value, value, 'test passed')
                    pass
                else:
                    print(value1, '--', value, value, 'test failed')
                    # print('choice', choice)
                    # print('answer', answer)

                # clean up user hands
                self.dealer.collectHandCards()
                self.user.collectHandCards()
                
    def testBasic(self):
        self.testSplits()
        # basicDict = {}
        # for i in range(1, 11):
        #     for j in range(1, 11):
        #         for k in range(1, 11):
        #             basicDict[(i, j, k)] = 5

        # for value in range(1, 11):
        #     for value1 in range(1, 11):
        #         for value2 in range(1, 11):
        #             # bet here
        #             # value = int(input("User first card value: "))
        #             # value1 = int(input("User second card value: "))
        #             # value2 = int(input("Dealer first card value: "))
        #             #deal hands out
        #             self.user.dealHand(self.shoe.createCard(value), self.shoe.createCard(value1))
        #             self.dealer.dealHand(self.shoe.createCard(value2), self.shoe.createCard(2))

        #             # self.dealer.printDealerUp()
        #             # self.dealer.printValue()

        #             # play basic strategy
        #             choice = playBasic(self.user, self.dealer, self.shoe)
        #             if choice == 'Sp':
        #                 print(value2, '--',value, value1)
        #             # self.user.printHand()

        #             # clean up user hands
        #             self.dealer.collectHandCards()
        #             self.user.collectHandCards()
               

    def play(self):
        
        # still haven't implemented dealer peeking and not implementing insurance
        # still haven't fixed user not hitting on H15 (5 10) against a dealer S11 (11 10)
        
        self.games_left = self.games_init
        while(self.games_left > 0):
            self.games_left -= 1
            # bet here
            self.user.startBet(1)
            
            #deal hands out
            self.dealer.dealHand(self.shoe.dealCard(), self.shoe.dealCard())
            self.user.dealHand(self.shoe.dealCard(), self.shoe.dealCard())

            self.dealer.printDealerUp()
            self.dealer.printValue()
            # self.user.printHand()

            # play basic strategy
            choice = playBasic(self.user, self.dealer, self.shoe)
            self.user.printHand()

            dealer_bust = 0
            if choice == 'Sp':
                self.user.makeDoubleBet()
                card_hold = self.user.hand.pop()
                choice = playSplit(self.user, self.dealer, self.shoe)
                self.user.printHand()
                result = self.checkNondependent(choice)
                if not result:
                    dealer_bust = playDealer(self.dealer, self.shoe)
                    self.checkDependent(choice, dealer_bust)
                self.user.collectHandCards()
                choice = playSplit1(self.user, self.dealer, self.shoe, card_hold)
                self.user.printHand()
                result = self.checkNondependent(choice)
                if not result:
                    self.checkDependent(choice, dealer_bust)

            else:
                # calculate who wins / update bet
                result = self.checkNondependent(choice)
                if not result:
                    dealer_bust = playDealer(self.dealer, self.shoe)
                    self.checkDependent(choice, dealer_bust)

            # clean up user hands
            self.user.resetBet()
            self.dealer.collectHandCards()
            self.user.collectHandCards()

    def printStats(self):
        print('**********************************************************')
        print('games:', self.games_init)
        print('blackjacks:', self.black_jacks)
        print('surrenders:', self.surrenders)
        print('blackjacks per game:', self.black_jacks / self.games_init)
        print('user wins:', self.user_wins)
        print('dealer wins:', self.dealer_wins)
        print('user wins / dealer wins:', self.user_wins / self.dealer_wins)
        print('user winnings:', self.user.winnings)
        print('dealer winnings:', self.dealer.winnings)
        print('dealer wins per game:', (self.dealer.winnings / self.games_init))
        print('**********************************************************')
