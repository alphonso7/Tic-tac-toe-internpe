board = ["-", "-", "-", "-", "-", "-","-", "-", "-"]
currentPlayer = "X"
runningGame = True
winner = None

def printBoard(board):
    print("      " + board[0] + "|" + board[1]+ "|" + board[2])
    print("      " + board[3] + "|" + board[4]+ "|" + board[5])
    print("      " + board[6] + "|" + board[7]+ "|" + board[8])
    
def Input(board):
    ip = int(input("Enter a number 1 to 9: "))
    if ip>=1 and ip<=9 and board[ip-1] == "-":
        board[ip-1] = currentPlayer
    else:
        print("Player has already marked there")
    
def checkHori(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= "-":
        winner = board[6]
        return True
def checkVert(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[3]!= "-":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[6]!= "-":
        winner = board[6]
        return True
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[3]!= "-":
        winner = board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        runningGame = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else: 
        currentPlayer = "X"

def checkForWin(board):
    if checkDiag(board) or checkHori(board) or checkVert(board):
        print(f"The winner is {winner}")

def computer(board):
    import random 
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while runningGame == True:
    printBoard(board)
    Input(board)
    checkForWin(board)
    checkTie(board)
    switchPlayer()
    checkForWin(board)
    checkTie(board)