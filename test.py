def makeSplitDict(pBasicDict):
    # init
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                pBasicDict[(i, j, k)] = '?'

    # aces and 8's
    for i in range(1, 11):
        pBasicDict[(i, 1, 1)] = 'Sp'
        pBasicDict[(i, 8, 8)] = 'Sp'

    # 10's
    for i in range(1, 11):
        pBasicDict[(i, 10, 10)] = 'S'
        
    # 9's
    for i in range(2, 7):
        pBasicDict[(i, 9, 9)] = 'Sp'
    pBasicDict[(7, 9, 9)] = 'S'
    for i in range(8, 10):
        pBasicDict[(i, 9, 9)] = 'Sp'
    pBasicDict[(10, 9, 9)] = 'S'
    pBasicDict[(1, 9, 9)] = 'S'

    # 7's
    for i in range(2, 8):
        pBasicDict[(i, 7, 7)] = 'Sp'
    for i in range(8, 11):
        pBasicDict[(i, 7, 7)] = 'H'
    pBasicDict[(1, 7, 7)] = 'H'

    # 6's
    for i in range(2, 7):
        pBasicDict[(i, 6, 6)] = 'Sp'
    for i in range(7, 11):
        pBasicDict[(i, 6, 6)] = 'H'
    pBasicDict[(1, 6, 6)] = 'H'
