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
    if pUser.value >= 19:
        return 'S'
    elif pUser.value == 18:
        if pDealer.hand[0].value == 2 or pDealer.hand[0].value == 7 or pDealer.hand[0].value == 8:
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

def playDealer(pDealer, pShoe):
    while pDealer.value < 21:
        if pDealer.value_type == 'H':
            # H 17+
            if pDealer.value >= 17:
                break
            else:
                pass
        else:
            # standing on Soft 17
            # S 17+
            if pDealer.value >= 17:
                break
            else:
                pass
        pDealer.hitHand(pShoe.dealCard())
        
    if pDealer.value > 21:
        return 1
    else:
        return 0

def playRestOfHand(pUser, pDealer, pShoe):
    while pUser.value < 21:
        if pUser.value_type == 'H':
            choice = checkHard(pUser, pDealer)
        else:
            choice = checkSoft(pUser, pDealer)

        # currently only surrenders and doubles on first choice
        if choice == 'U' or choice == 'D':
            choice = 'H'
            
        if choice == 'S':
            break
        
        if choice == 'H':
            pUser.hitHand(pShoe.dealCard())

    if pUser.value > 21:
        choice = 'Bu'

    return choice

def playTestHand(pUser, pDealer, pShoe):
    # pUser.printHand()
    if pUser.value_type == 'S':
        # check for black jack
        if pUser.value == 21 :
            return 'Bj'

        choice = checkSoft(pUser, pDealer)

    else:
        # check for surrender
        choice = checkHard(pUser, pDealer)
        if choice == 'U':
            return 'Su'
        
    if choice == 'D':
        pUser.hitHand(pShoe.dealCard())
        return 'D'

    if pUser.value_type == 'H':
        choice = checkHard(pUser, pDealer)
    else:
        choice = checkSoft(pUser, pDealer)

    return choice

    
def playHand(pUser, pDealer, pShoe):
    if pUser.value_type == 'S':
        # check for black jack
        if pUser.value == 21 :
            return 'Bj'
        
        choice = checkSoft(pUser, pDealer)

    else:
        choice = checkHard(pUser, pDealer)
        # check for surrender
        if choice == 'U':
            return 'Su'

    if choice == 'D':
        pUser.hitHand(pShoe.dealCard())
        return 'D'

    choice = playRestOfHand(pUser, pDealer, pShoe)

    return choice

def playSplit(pUser, pDealer, pShoe):
    # adjust for first hand
    pUser.hitHand(pShoe.dealCard())
    print("First split cards are..")
    pUser.printHand()
    return playHand(pUser, pDealer, pShoe)            
        
# calculate and collect for first hand
# cannot calculate for now
def playSplit1(pUser, pDealer, pShoe, pCard_Hold):
    # adjust for second hand
    print("Second split cards are..")
    pUser.hitHand(pCard_Hold)
    pUser.hitHand(pShoe.dealCard())
    pUser.printHand()
    return playHand(pUser, pDealer, pShoe)

def playTestBasic(pUser, pDealer, pShoe):
    # check for split
    # check for 11 becuase two aces will be a S12 and not H22
    if pUser.hand[0].value == pUser.hand[1].value or (pUser.hand[0].value == 11 and pUser.hand[1].value == 1):
        choice = checkSplit(pUser, pDealer)
        # print("User chose to--------------------:", choice)
        if choice == 'P':
            return 'Sp'

    return playTestHand(pUser, pDealer, pShoe)

def playBasic(pUser, pDealer, pShoe):
    # check for split
    # check for 11 becuase two aces will be a S12 and not H22
    if pUser.hand[0].value == pUser.hand[1].value or (pUser.hand[0].value == 11 and pUser.hand[1].value == 1):
        choice = checkSplit(pUser, pDealer)
        # print("User chose to--------------------:", choice)
        if choice == 'P':
            return 'Sp'

    return playHand(pUser, pDealer, pShoe)
