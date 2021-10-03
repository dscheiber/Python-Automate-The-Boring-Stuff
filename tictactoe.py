##this is a game of tictactoe, assembled before watching the video about data structures.
#i thought it would be a nice challenge

import random

gameOver = 0
roundCount = 0
playerTeam = "X"
AITeam = "O"
turnOrder = []
AIdifficulty = "normal"


gameBoard = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': '_',
    'mid-mid': '_',
    'mid-right': '_',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': '_'
}
##test condition, bot 1 away from winning
gameBoardTest1 = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': '_',
    'mid-mid': '_',
    'mid-right': 'O',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': 'O'
}

##test condition, bot cannot acquire middle
gameBoardTest2 = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': '_',
    'mid-mid': 'X',
    'mid-right': '_',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': '_'
}
##test condition, bot has options after acquiring middle
gameBoardTest3 = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': '_',
    'mid-mid': 'O',
    'mid-right': '_',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': '_'
}





gameBoardTranslation = {
    'top-horizontal' : ['top-left', 'top-mid','top-right'],
    'mid-horizontal' : ['mid-left','mid-mid','mid-right'],
    'bot-horizontal' : ['bot-left','bot-mid','bot-right'],
    'left-vertical' : ['top-left','mid-left','bot-left'],
    'mid-vertical' : ['top-mid','mid-mid','bot-mid'],
    'right-vertical' : ['top-right','mid-right','bot-right'],
    'forward-slash' : ['bot-left','mid-mid','top-right'],
    'backward-slash' : ['top-left','mid-mid','bot-right']    
}

def display(gameBoard):
    print('_', gameBoard['top-left'], '_|_', gameBoard['top-mid'], '_|_', gameBoard['top-right'], '_')
    print('_', gameBoard['mid-left'], '_|_', gameBoard['mid-mid'], '_|_', gameBoard['mid-right'], '_')
    print('_', gameBoard['bot-left'], '_|_', gameBoard['bot-mid'], '_|_', gameBoard['bot-right'], '_')

def scoring(gameBoard):
    global gameOver
    placement = {}
    placement.update({'top-horizontal' : gameBoard['top-left']+gameBoard['top-mid']+gameBoard['top-right']})
    placement.update({'mid-horizontal' : gameBoard['mid-left']+gameBoard['mid-mid']+gameBoard['mid-right']})
    placement.update({'bot-horizontal' : gameBoard['bot-left']+gameBoard['bot-mid']+gameBoard['bot-right']})
    placement.update({'left-vertical' : gameBoard['top-left']+gameBoard['mid-left']+gameBoard['bot-left']})
    placement.update({'mid-vertical' : gameBoard['top-mid']+gameBoard['mid-mid']+gameBoard['bot-mid']})
    placement.update({'right-vertical' : gameBoard['top-right']+gameBoard['mid-right']+gameBoard['bot-right']})
    placement.update({'forward-slash' : gameBoard['bot-left']+gameBoard['mid-mid']+gameBoard['top-right']})
    placement.update({'backward-slash' : gameBoard['top-left']+gameBoard['mid-mid']+gameBoard['bot-right']})
    print(placement)
    
    for scoreString in placement.values():
        scoreX = scoreString.count('X')
        scoreO = scoreString.count('O')
        if scoreX == 3:
            print('X wins!')
            gameOver = 1     
        elif scoreO == 3:
            print('O wins!')
            gameOver = 1

            

def mark(gameBoard):
    print('It\'s your turn.')
    markValidated = 0
    while markValidated == 0:
        try:
            mark = input('Choose a square. \n')
            gameBoard[mark] ##checks to see if entry is in dict; throws error if not
            if gameBoard[mark] == "_":
                gameBoard[mark] = playerTeam
                markValidated = 1
            else:
                print("You cannot select a square that has been previously occupied. Try again.")
        except:
            print('''Not a valid input. Valid input options include: \n
                'top-left', 'top-mid','top-right', \n
                'mid-left', 'mid-mid','mid-right', \n
                'bot-left', 'bot-mid', 'bot-right'.''')

def AIturn(gameBoard):
    print('Enemys turn.')
    freeSpaces = []
    for name, currentState in gameBoard.items():
        if currentState == '_':
            freeSpaces.append(name)
    randomChoice = random.randint(0, len(freeSpaces)-1)
    gameBoard[freeSpaces[randomChoice]] = AITeam

def chooseSide():
    global playerTeam, AITeam
    while playerTeam == "unset":
        playerTeam = input("Choose a marker: X or O. \n").upper()
        #print(playerTeam)
        if playerTeam != "X" and playerTeam != "O":
            print('Choose X or O and not anything dumb, please. Try again.')
            playerTeam = "unset"
    if playerTeam == "X":
        AITeam = "O"
    else:
        AITeam = "X"
    #print("Player", playerTeam, "AI", AITeam)

def defineTurnOrder():
    global turnOrder
    turnDefine = random.randint(0,1)
    if turnDefine == 0:
        turnOrder = ['Player', 'AI']
    else:
        turnOrder = ['AI', 'Player']
    print(turnOrder[0],'will go first.')

def AIHardTurn(gameBoard):
    placement = {}
    nextMove = ""
    nextMoveList = []
    placement.update({'top-horizontal' : gameBoard['top-left']+gameBoard['top-mid']+gameBoard['top-right']})
    placement.update({'mid-horizontal' : gameBoard['mid-left']+gameBoard['mid-mid']+gameBoard['mid-right']})
    placement.update({'bot-horizontal' : gameBoard['bot-left']+gameBoard['bot-mid']+gameBoard['bot-right']})
    placement.update({'left-vertical' : gameBoard['top-left']+gameBoard['mid-left']+gameBoard['bot-left']})
    placement.update({'mid-vertical' : gameBoard['top-mid']+gameBoard['mid-mid']+gameBoard['bot-mid']})
    placement.update({'right-vertical' : gameBoard['top-right']+gameBoard['mid-right']+gameBoard['bot-right']})
    placement.update({'forward-slash' : gameBoard['bot-left']+gameBoard['mid-mid']+gameBoard['top-right']})
    placement.update({'backward-slash' : gameBoard['top-left']+gameBoard['mid-mid']+gameBoard['bot-right']})
    print(placement)
    
    for location, scoreString in placement.items():
        scoreAI = scoreString.count(AITeam)
        if scoreAI == 2:
            for placement in range(len(scoreString)):
                if scoreString[placement] == "_":
                    nextMoveList.append(gameBoardTranslation[location][placement])
                    nextMove = nextMoveList[random.randint(0, len(nextMoveList)-1)]
                    print(nextMove)
                    return nextMove
        elif scoreAI == 1:
            for placement in range(len(scoreString)):
                if scoreString[placement] == "_" and (gameBoardTranslation[location][placement] == 'top-left' or gameBoardTranslation[location][placement] == 'top-right' or gameBoardTranslation[location][placement] == 'bot-left' or gameBoardTranslation[location][placement] == 'bot-right'):
                    nextMoveList.append(gameBoardTranslation[location][placement])
            nextMove = nextMoveList[random.randint(0, len(nextMoveList)-1)]
            print(nextMove)
            return nextMove
    if len(nextMove) == 0:
        if gameBoard['mid-mid'] == "_":
            nextMove = "mid-mid"
        if gameBoard['top-left'] == "_":
            nextMoveList.append('top-left')
        if gameBoard['top-right'] == "_":
            nextMoveList.append('top-right')
        if gameBoard['bot-left'] == "_":
            nextMoveList.append('bot-left')
        if gameBoard['bot-right'] == "_":
            nextMoveList.append('bot-right')
        print(nextMoveList)
    if len(nextMove) == 0:
        nextMove = nextMoveList[random.randint(0, len(nextMoveList)-1)]
    print(nextMove)
    return nextMove
            

AIHardTurn(gameBoardTest3)


# ##game start

# print('Welcome to a cool game of tic tac toe made durinng my son\'s nap!')
# chooseSide()
# defineTurnOrder()
# display(gameBoard)

# ##main game loop
# while gameOver != 1:
#     roundCount += 1
#     print('Round',roundCount)
#     ##first turn of loop
#     if turnOrder[0] == 'Player':
#         mark(gameBoard)
#     else:
#         AIturn(gameBoard)
#     display(gameBoard)
#     scoring(gameBoard)
#     ##second turn of loop
#     if turnOrder[1] == 'Player':
#         mark(gameBoard)
#     else:
#         AIturn(gameBoard)
#     display(gameBoard)
#     scoring(gameBoard)

# print('Thanks for playing.')