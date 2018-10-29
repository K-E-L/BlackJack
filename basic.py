def checkHard(pUser, pDealer):
    # H 17+
    if pUser.value >= 17:
        return 'S'
    # H 8 - 
    if pUser.value <= 8:
        return 'H'
    # H 16 through 12
    elif pUser.value >= 13 and pDealer.hand[0].value <= 6:
        return 'S'
    elif pUser.value >= 13 and pDealer.hand[0].value > 6:
        if pUser.value == 16 and pDealer.hand[0].value >= 9:
            return 'U'
        elif pUser.value == 15 and pDealer.hand[0].value == 10:
            return 'U'
        else:
            return 'H'
    elif pUser.value == 12:
        if pDealer.hand[0].value <= 3:
            return 'H'
        elif pDealer.hand[0].value > 6:
            return 'H'
        else:
            return 'S'
        # H 11 through 9
    elif pUser.value == 11:
        if pDealer.hand[0].value == 11:
            return 'H'
        else:
            return 'D'
    elif pUser.value == 10:
        if pDealer.hand[0].value >= 10:
            return 'H'
        else:
            return 'D'
    elif pUser.value == 9:
        if pDealer.hand[0].value >= 7:
            return 'H'
        elif pDealer.hand[0].value == 2:
            return 'H'
        else:
            return 'D'

def checkSoft(pUser, pDealer):
    # elif pUser.value >= 13 and pDealer.hand[0].value <= 6:
    #     return 'S'
    if pUser.value >= 19:
        return 'S'
    elif pUser.value == 18:
        if pDealer.hand[0].value == 2 or pDealer.hand[0].value ==  7 or pDealer.hand[0].value == 8:
            return 'S'
        elif pDealer.hand[0].value >= 9:
            return 'H'
        else:
            return 'D'
    elif pUser.value == 17:
        if pDealer.hand[0].value >= 7:
            return 'H'
        elif pDealer.hand[0].value == 2:
            return 'H'
        else:
            return 'D'
    elif pUser.value == 15 or pUser.value == 16:
        if pDealer.hand[0].value >= 7:
            return 'H'
        elif pDealer.hand[0].value <= 3:
            return 'H'
        else:
            return 'D'
    else:
        if pDealer.hand[0].value >= 7:
            return 'H'
        elif pDealer.hand[0].value <= 4:
            return 'H'
        else:
            return 'D'

def checkSplit(pUser, pDealer):
    if pUser.hand[0].value == 11 or pUser.hand[0].value == 8:
        return 'P'
    elif pUser.hand[0].value == 10:
        return 'S'
    elif pUser.hand[0].value == 9:
        if pDealer.hand[0].value == 7 or pDealer.hand[0].value >= 10:
            return 'S'
        else:
            return 'P'
    elif pUser.hand[0].value == 6:
        if pDealer.hand[0].value >= 7:
            return 'H'
        else:
            return 'P'
    elif pUser.hand[0].value == 4:
        if pDealer.hand[0].value >= 7:
            return 'H'
        elif pDealer.hand[0].value <= 4:
            return 'H'
        else:
            return 'P'
    elif pUser.hand[0].value == 5:
        if pDealer.hand[0].value >= 10:
            return 'H'
        else:
            return 'D'
    else:
        if pDealer.hand[0].value >= 8:
            return 'H'
        else:
            return 'P'

def playHand(pUser, pDealer, pShoe):
    # while pUser.value < 21:
    while pUser.value < 21:
        if pUser.value_type == 'H':
            choice = checkHard(pUser, pDealer)
        else:
            choice = checkSoft(pUser, pDealer)

        print("User chose to:", choice)

        if choice == 'S' or choice == 'D' or choice == 'U':
            break
        
        if choice == 'H':
            pUser.hitHand(pShoe.dealCard())

def playBasic(pUser, pDealer, pShoe):
    # haven't added surrenders yet
    first_hand = True
    # haven't done splits yet

    # check for black jack
    if pUser.value == 21 and pUser.value_type == 'S':
        print("User blackjack")
        return 'Bj'

    # check for surrender
    choice = checkHard(pUser, pDealer)
    if choice == 'U':
        return 'Su'

    # check for split
    if pUser.hand[0].value == pUser.hand[1].value:
        choice = checkSplit(pUser, pDealer)
        print("User chose to--------------------:", choice)

        if choice == 'P':
            # adjust for first hand
            card_hold = pUser.hand.pop()
            pUser.hitHand(pShoe.dealCard())
            print("First split cards are..")
            pDealer.printDealerUp()
            pUser.printHand("user")
            playHand(pUser, pDealer, pShoe)

            # calculate and collect for first hand
            # cannot calculate for now
            # won = self.calculateGame(pDealer.value, pUser.value)
            # self.calculateBet(won)
            pDealer.collectHandCards()
            pUser.collectHandCards()

            # adjust for second hand
            print("Second split cards are..")
            pDealer.dealHand(pShoe.dealCard(), pShoe.dealCard())
            pUser.hitHand(card_hold)
            pUser.hitHand(pShoe.dealCard())
            pDealer.printDealerUp()
            pUser.printHand("user")
            playHand(pUser, pDealer, pShoe)
        

    else:
        playHand(pUser, pDealer, pShoe)
        
    if pUser.value > 21:
        print("User busted")
        return 'Bu'
