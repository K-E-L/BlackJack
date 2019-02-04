from cards import *
from players import *
from basic import *
from testBasic import *

class Game:
    def __init__(self, pSystem, pDeckCount, pCardsCut, pSpread, pBetDuringNegativeCount):
        self.shoe = Shoe(pSystem, pDeckCount, pCardsCut)
        self.dealer = Player('dealer', pSpread, pBetDuringNegativeCount)
        self.user = Player('user', pSpread, pBetDuringNegativeCount)

        self.dealer_wins = 0
        self.user_wins = 0

        # self.games_init = int(input("Enter how many games to play: "))
        # currently 1000000 games per ~53 sec. on razer 15
        self.games_init = 1000000
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
        self.dealer.printHand()

        if pDealer_Bust:
            print('dealer busted')
            
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

                
    def play(self):        
        self.games_left = self.games_init
        while(self.games_left > 0):
            self.games_left -= 1
            self.shoe.checkCutForShuffle()
            
            # bet here
            # self.user.startBet(1)
            self.user.systemBet(self.shoe, self.user.diff_from_true_count)

            # max true count (6 deck shoe, 1 deck cut)  --  31 32 29 30 33 34 33 35 36 36
            
            # (6 deck shoe, 1 deck cut, spread of 50)
            # average bet      -- 1.63    - Hi-Lo: by simply adding 0 to the bet
            # average winnings -- .0417   - mapping to spread 1-50 
            # average edge     -- .0253   - setting the max at 50


            # .025985 deck estimation 0
            
            
            # deal hands out
            self.dealer.dealHand(self.shoe.dealCard(), self.shoe.dealCard())
            if (self.dealer.hand[0].value == 11 and self.dealer.hand[1].value == 10) or (self.dealer.hand[0].value == 10 and self.dealer.hand[1].value == 11):
                # don't take insurance, lose instead
                print("user doesn't take insurance and dealer blackjacks")
                self.dealer.printHand()
                self.dealer.wins(self.user.bet)
                self.user.loses(self.user.bet)
                self.user_wins -= 1
            
            else:
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
        print('decks:', self.shoe.deck_count)
        print('cards cut:', self.shoe.cards_cut)
        print('spread:', self.user.spread)
        print('bet negative:', self.user.bet_during_negative_count)
        print('system:', self.shoe.system.name)
        print('games:', self.games_init)
        print('blackjacks:', self.black_jacks)
        print('surrenders:', self.surrenders)
        print('blackjacks per game:', self.black_jacks / self.games_init)
        print('user wins:', self.user_wins)
        print('dealer wins:', self.dealer_wins)
        print('max running count', self.shoe.system.max_running_count)
        print('min running count', self.shoe.system.min_running_count)
        print('max true count', self.shoe.system.max_true_count)
        print('min true count', self.shoe.system.min_true_count)
        print('average true count:', self.shoe.system.total_true_count / self.games_init)
        print('highest betting unit:', self.user.max_bet)
        print('average bet:', self.user.total_bet / self.games_init)
        if self.user.total_bet != 0:
            print('average user edge', ((self.user.winnings / self.games_init) / (self.user.total_bet / self.games_init)))
        print('**********************************************************')

    def fileStats(self):
        f = open("output.txt", "a")
        f.write('system: ' + str(self.shoe.system.name) + '\n')
        f.write('decks: ' + str(self.shoe.deck_count) + '\n')
        f.write('spread: ' + str(self.user.spread) + '\n')
        f.write('bet negative: ' + str(self.user.bet_during_negative_count) + '\n')
        f.write('average user edge: ' + str((self.user.winnings / self.games_init) / (self.user.total_bet / self.games_init)) + '\n')


        
# -------- testing functions --------------------------------------------------------------------


    # need to update for hi-lo betting 
    def testPlayOne(self):
        value = int(input("User first card value: "))
        value1 = int(input("User second card value: "))
        value2 = int(input("Dealer first card value: "))
        value3 = int(input("Dealer second card value: "))
    
        # bet here
        self.user.startBet(1)
        
        # deal hands out
        self.dealer.dealHand(self.shoe.createCard(value2), self.shoe.createCard(value3))
        self.user.dealHand(self.shoe.createCard(value), self.shoe.createCard(value1))

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

    def testBasic(self):
        basicDict = {}
        makeDict(basicDict)
        for value in range(1, 11):
            for value1 in range(1, 11):
                for value2 in range(1, 11):
                    # deal hands out
                    self.user.dealHand(self.shoe.createCard(value), self.shoe.createCard(value1))
                    # (2) because dealer down card doesn't really matter
                    self.dealer.dealHand(self.shoe.createCard(value2), self.shoe.createCard(2))

                    # play basic strategy
                    choice = playTestBasic(self.user, self.dealer, self.shoe)
                    answer = basicDict[(value2, value, value1)]
                    if (choice == answer):
                        # self.user.printHand()
                        # print(value2, '--', value, value1, 'test passed')
                        pass
                    else:
                        # self.user.printHand()
                        print(value2, '--', value, value1, 'test failed')
                        # print('choice', choice)
                        # print('answer', answer)
                        pass

                    # clean up user hands
                    self.dealer.collectHandCards()
                    self.user.collectHandCards()
