##this is a game of tictactoe, assembled before watching the video about data structures.
#i thought it would be a nice challenge

import random

gameOver = 0
roundCount = 0
playerTeam = "unset"
AITeam = "unset"
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

##instructions for gameboard inputs
gameBoardInstructions = {
    'top-left': 'top-left',
    'top-mid': 'top-mid',
    'top-right': 'top-right',
    'mid-left': 'mid-left',
    'mid-mid': 'mid-mid',
    'mid-right': 'mid-right',
    'bot-left': 'bot-left',
    'bot-mid': 'bot-mid',
    'bot-right': 'bot-right'
}

##reconciles gameboard vs placement indexes used for AI turns
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
    filledConditions = 0
    placement = {}
    placement.update({'top-horizontal' : gameBoard['top-left']+gameBoard['top-mid']+gameBoard['top-right']})
    placement.update({'mid-horizontal' : gameBoard['mid-left']+gameBoard['mid-mid']+gameBoard['mid-right']})
    placement.update({'bot-horizontal' : gameBoard['bot-left']+gameBoard['bot-mid']+gameBoard['bot-right']})
    placement.update({'left-vertical' : gameBoard['top-left']+gameBoard['mid-left']+gameBoard['bot-left']})
    placement.update({'mid-vertical' : gameBoard['top-mid']+gameBoard['mid-mid']+gameBoard['bot-mid']})
    placement.update({'right-vertical' : gameBoard['top-right']+gameBoard['mid-right']+gameBoard['bot-right']})
    placement.update({'forward-slash' : gameBoard['bot-left']+gameBoard['mid-mid']+gameBoard['top-right']})
    placement.update({'backward-slash' : gameBoard['top-left']+gameBoard['mid-mid']+gameBoard['bot-right']})
    
    for scoreString in placement.values():
        scoreX = scoreString.count('X')
        scoreO = scoreString.count('O')
        scoreUnderline = scoreString.count('_')
        if scoreX == 3:
            print('X wins!')
            gameOver = 1     
        elif scoreO == 3:
            print('O wins!')
            gameOver = 1
        
        ##end the game if the board fills
        elif scoreUnderline == 0:
            filledConditions += 1
            if filledConditions == 8:
                print('Tie game, everybody loses.')
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
    print('Enemy\'s', AIdifficulty, 'turn.')
    freeSpaces = []
    if AIdifficulty == "hard":
        choice = AIHardTurn(gameBoard)
        try:
            gameBoard[choice] = AITeam
        except:
            print('error in hard turn')

            gameBoard[freeSpaces[choice]] = AITeam
    else:
        for name, currentState in gameBoard.items():
            if currentState == '_':
                freeSpaces.append(name)
        choice = random.randint(0, len(freeSpaces)-1)
        gameBoard[freeSpaces[choice]] = AITeam

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
    nextMoveListBlock = []
    placement.update({'top-horizontal' : gameBoard['top-left']+gameBoard['top-mid']+gameBoard['top-right']})
    placement.update({'mid-horizontal' : gameBoard['mid-left']+gameBoard['mid-mid']+gameBoard['mid-right']})
    placement.update({'bot-horizontal' : gameBoard['bot-left']+gameBoard['bot-mid']+gameBoard['bot-right']})
    placement.update({'left-vertical' : gameBoard['top-left']+gameBoard['mid-left']+gameBoard['bot-left']})
    placement.update({'mid-vertical' : gameBoard['top-mid']+gameBoard['mid-mid']+gameBoard['bot-mid']})
    placement.update({'right-vertical' : gameBoard['top-right']+gameBoard['mid-right']+gameBoard['bot-right']})
    placement.update({'forward-slash' : gameBoard['bot-left']+gameBoard['mid-mid']+gameBoard['top-right']})
    placement.update({'backward-slash' : gameBoard['top-left']+gameBoard['mid-mid']+gameBoard['bot-right']})
    
    for location, scoreString in placement.items():
        scoreAI = scoreString.count(AITeam)
        scorePlayer = scoreString.count(playerTeam)
        scoreUnderline = scoreString.count('_')

        ##bot 1 away from winning, functions to win
        if scoreAI == 2 and scorePlayer == 0:
            for placement in range(len(scoreString)):
                if scoreString[placement] == "_":
                    nextMove = gameBoardTranslation[location][placement]
                    return nextMove

        ##player 1 away from winning, functions to block            
        if scorePlayer == 2 and scoreUnderline == 1 and scoreAI == 0:
            for placement in range(len(scoreString)):
                if scoreString[placement] == "_":
                    nextMoveListBlock.append(gameBoardTranslation[location][placement])


        ##2 away from winning; only 1 item placed but makes a meaningful move            
        elif scoreAI == 1 and scoreUnderline > 0:
            for placement in range(len(scoreString)):
                if scoreString[placement] == "_" and (gameBoardTranslation[location][placement] == 'top-left' or gameBoardTranslation[location][placement] == 'top-right' or gameBoardTranslation[location][placement] == 'bot-left' or gameBoardTranslation[location][placement] == 'bot-right' or gameBoardTranslation[location][placement] == 'mid-mid'):
                    nextMoveList.append(gameBoardTranslation[location][placement])
    
    ## chooses between blocking moves or lesser move                    
    if len(nextMoveListBlock) > 0:
        nextMove = nextMoveListBlock[random.randint(0, len(nextMoveListBlock)-1)]
        return nextMove
    elif len(nextMoveList) > 0:
        nextMove = nextMoveList[random.randint(0, len(nextMoveList)-1)]
        return nextMove

        ##first move, chooses only good spots
    if scoreAI == 0 and (scorePlayer == 0 or scorePlayer == 1):
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
    
    if len(nextMoveList) > 0:
        nextMove = nextMoveList[random.randint(0, len(nextMoveList)-1)]
        return nextMove
    else:
        freeSpaces = []
        for name, currentState in gameBoard.items():
            if currentState == '_':
                freeSpaces.append(name)
        nextMove = random.randint(0, len(freeSpaces)-1)
        return nextMove

def difficultySelect():
    global AIdifficulty
    difficultyUnselected = 0
    while difficultyUnselected == 0:
        difficultyChoice = input("Do you want to play on normal or hard? \n")
        if difficultyChoice == "normal" or difficultyChoice == "hard":
            difficultyUnselected = 1
            AIdifficulty = difficultyChoice
            return
        else:
            print('That is not a valid difficulty option.')
            

##main game loop
def gameLoop(gameBoard):
    roundCount = 0
    while gameOver != 1:
        roundCount += 1
        print('Round',roundCount)

        ##first turn of the round
        if turnOrder[0] == 'Player':
            mark(gameBoard)
        else:
            AIturn(gameBoard)
        display(gameBoard)
        scoring(gameBoard)
        if gameOver == 1:
            break
        ##second turn of the round
        if turnOrder[1] == 'Player':
            mark(gameBoard)
        else:
            AIturn(gameBoard)
        display(gameBoard)
        scoring(gameBoard)            

#game start

print('Welcome to a cool game of tic tac toe made during my son\'s nap!')
chooseSide()
difficultySelect()
defineTurnOrder()
print('Enter the below values to choose your squares. Good luck!')
display(gameBoardInstructions)
gameLoop(gameBoard)
print('Thanks for playing.')


###test gameBoards below for testing AI behavior
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

##test condition, bot has a non-middle single space
gameBoardTest4 = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': '_',
    'mid-mid': '_',
    'mid-right': '_',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': 'O'
}

##test condition, player is 1 away from winning
gameBoardTest5 = {
    'top-left': '_',
    'top-mid': '_',
    'top-right': '_',
    'mid-left': 'X',
    'mid-mid': 'X',
    'mid-right': '_',
    'bot-left': '_',
    'bot-mid': '_',
    'bot-right': '_'
}

##test condition, player is 1 away from winning in two ways
gameBoardTest6 = {
    'top-left': 'X',
    'top-mid': '_',
    'top-right': 'O',
    'mid-left': '_',
    'mid-mid': 'X',
    'mid-right': 'X',
    'bot-left': 'O',
    'bot-mid': 'X',
    'bot-right': 'O'
}

##blank gameboard
gameBoardBlank = {
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