board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True
gameWinning = False
new_board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

# print the game board


def printBoard(board):
    print(board[0]+"|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3]+"|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6]+"|" + board[7] + "|" + board[8])
# printBoard(board)

# take player input


def playerInput(board):
    user_input = int(input("Input a number 1-9: "))
    if 9 >= user_input >= 1 and board[user_input-1 == "="]:
        board[user_input-1] = currentPlayer
    else:
        print("That spot has been chosen.")

# check for win or tie


def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[6]
        return True


def checkAngle(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie! ")
        gameRunning = False


def checkWin():
    global gameWinning
    if checkAngle(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameWinning = True

# switch the player


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# check for winner or tie again


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    if gameWinning is True:
        printBoard(board)
        print("New game:... ")
        board = new_board
        gameWinning = False
