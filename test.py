def makeDict(pBasicDict):
    makeDictInit(pBasicDict)
    makeDictSplits(pBasicDict)
    makeDictSofts(pBasicDict)
    makeDictHards(pBasicDict)

def makeDictInit(pBasicDict):
    # init
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                pBasicDict[(i, j, k)] = '?'

def makeDictSplits(pBasicDict):
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

    # 5's
    for i in range(2, 10):
        pBasicDict[(i, 5, 5)] = 'D'
    for i in range(10, 11):
        pBasicDict[(i, 5, 5)] = 'H'
    pBasicDict[(1, 5, 5)] = 'H'

    # 4's
    for i in range(2, 5):
        pBasicDict[(i, 4, 4)] = 'H'
    for i in range(5, 7):
        pBasicDict[(i, 4, 4)] = 'Sp'
    for i in range(7, 11):
        pBasicDict[(i, 4, 4)] = 'H'
    pBasicDict[(1, 4, 4)] = 'H'
    
    # 3's
    for i in range(2, 8):
        pBasicDict[(i, 3, 3)] = 'Sp'
    for i in range(8, 11):
        pBasicDict[(i, 3, 3)] = 'H'
    pBasicDict[(1, 3, 3)] = 'H'
    
    # 2's
    for i in range(2, 8):
        pBasicDict[(i, 2, 2)] = 'Sp'
    for i in range(8, 11):
        pBasicDict[(i, 2, 2)] = 'H'
    pBasicDict[(1, 2, 2)] = 'H'
    

def makeDictSofts(pBasicDict):
    # black jacks
    for i in range(1, 11):
        for j in range(10, 11):
            pBasicDict[(i, j, 1)] = 'Bj'
            pBasicDict[(i, 1, j)] = 'Bj'
        
    # 8's to 10's
    for i in range(1, 11):
        for j in range(8, 10):
            pBasicDict[(i, j, 1)] = 'S'
            pBasicDict[(i, 1, j)] = 'S'

    # 7's
    for i in range(2, 3):
        pBasicDict[(i, 7, 1)] = 'S'
        pBasicDict[(i, 1, 7)] = 'S'
    for i in range(3, 7):
        pBasicDict[(i, 7, 1)] = 'D'
        pBasicDict[(i, 1, 7)] = 'D'
    for i in range(7, 9):
        pBasicDict[(i, 7, 1)] = 'S'
        pBasicDict[(i, 1, 7)] = 'S'
    for i in range(9, 11):
        pBasicDict[(i, 7, 1)] = 'H'
        pBasicDict[(i, 1, 7)] = 'H'
    for i in range(1, 2):
        pBasicDict[(i, 7, 1)] = 'H'
        pBasicDict[(i, 1, 7)] = 'H'

    # 6's
    for i in range(2, 3):
        pBasicDict[(i, 6, 1)] = 'H'
        pBasicDict[(i, 1, 6)] = 'H'
    for i in range(3, 7):
        pBasicDict[(i, 6, 1)] = 'D'
        pBasicDict[(i, 1, 6)] = 'D'
    for i in range(7, 11):
        pBasicDict[(i, 6, 1)] = 'H'
        pBasicDict[(i, 1, 6)] = 'H'
    for i in range(1, 2):
        pBasicDict[(i, 6, 1)] = 'H'
        pBasicDict[(i, 1, 6)] = 'H'

    # 4's and 5's
    for j in range(4, 6):
        for i in range(2, 4):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'
        for i in range(4, 7):
            pBasicDict[(i, j, 1)] = 'D'
            pBasicDict[(i, 1, j)] = 'D'
        for i in range(7, 11):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'
        for i in range(1, 2):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'

    # 3's and 2's
    for j in range(2, 4):
        for i in range(2, 5):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'
        for i in range(5, 7):
            pBasicDict[(i, j, 1)] = 'D'
            pBasicDict[(i, 1, j)] = 'D'
        for i in range(7, 11):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'
        for i in range(1, 2):
            pBasicDict[(i, j, 1)] = 'H'
            pBasicDict[(i, 1, j)] = 'H'
    
def makeDictHards(pBasicDict):
    # init
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                if(pBasicDict[(i, j, k)] == '?'):
                    # 17+'s
                    if(j + k >= 17):
                        for i in range(1, 11):
                            pBasicDict[(i, j, k)] = 'S'
                    # 13's to 16's
                    if(j + k >= 13 and j + k <= 16):
                        for i in range(2, 7):
                            pBasicDict[(i, j, k)] = 'S'
                        for i in range(7, 11):
                            pBasicDict[(i, j, k)] = 'H'
                        for i in range(1, 2):
                            pBasicDict[(i, j, k)] = 'H'
                    # 12's
                    if(j + k == 12):
                        for i in range(1, 4):
                            pBasicDict[(i, j, k)] = 'H'
                        for i in range(4, 7):
                            pBasicDict[(i, j, k)] = 'S'
                        for i in range(7, 11):
                            pBasicDict[(i, j, k)] = 'H'
                    # 11's
                    if(j + k == 11):
                        for i in range(2, 11):
                            pBasicDict[(i, j, k)] = 'D'
                        for i in range(1, 2):
                            pBasicDict[(i, j, k)] = 'H'
                    # 10's
                    if(j + k == 10):
                        for i in range(2, 10):
                            pBasicDict[(i, j, k)] = 'D'
                        for i in range(10, 11):
                            pBasicDict[(i, j, k)] = 'H'
                        for i in range(1, 2):
                            pBasicDict[(i, j, k)] = 'H'
                    # 9's
                    if(j + k == 9):
                        for i in range(2, 3):
                            pBasicDict[(i, j, k)] = 'H'
                        for i in range(3, 7):
                            pBasicDict[(i, j, k)] = 'D'
                        for i in range(7, 11):
                            pBasicDict[(i, j, k)] = 'H'
                        for i in range(1, 2):
                            pBasicDict[(i, j, k)] = 'H'
                    # 5's to 8's
                    if(j + k >= 5 and j + k <= 8):
                        for i in range(1, 11):
                            pBasicDict[(i, j, k)] = 'H'

                    # surrenders
                    if(j + k == 16):
                        for i in range(9, 11):
                            pBasicDict[(i, j, k)] = 'Su'
                        for i in range(1, 2):
                            pBasicDict[(i, j, k)] = 'Su'
                    if(j + k == 15):
                        for i in range(10, 11):
                            pBasicDict[(i, j, k)] = 'Su'
