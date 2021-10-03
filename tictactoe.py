##this is a game of tictactoe, assembled before watching the video about data structures.
#i thought it would be a nice challenge

import random

gameOver = 0
roundCount = 0

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
            gameBoard[mark] = 'X'
            markValidated = 1
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
    gameBoard[freeSpaces[randomChoice]] = 'O'

print('Welcome to a cool game of tic tac toe made durinng my son\'s nap!')
while gameOver != 1:
    roundCount += 1
    print('Round',roundCount)
    display(gameBoard)
    mark(gameBoard)
    AIturn(gameBoard)
    scoring(gameBoard)

print('Thanks for playing.')