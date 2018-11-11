# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Roxy Lai
# Created: November 8th, 2018
# 1 = first player
# 2 = second player
# 0 = blank square

symbol = [" ", "x", "o"]
player1 = 1
player2 = 2
blank = 0


def printRow(row):
    print("|", end=" ")
    for cell in row:
        print("" + symbol[cell] + " |", end=" ")
    print("")


def printBoard(board):
    # print the top border
    print("+-----------+")
    for rowNumber in range(0, 3):
        printRow(board[rowNumber])
        print("+-----------+")
    # for each row in the board...
    # print the row


def markBoard(board, rowNumber, colNumber, playerNumber):
    # check to see whether the desired square is blank, if is set to player number
    # return a boolean indicating whether the user chose a blank cell
    if board[rowNumber][colNumber] == 0:
        board[rowNumber][colNumber] = playerNumber
        return True
    else:
        print("That space is already taken!")
        return False


def getPlayerMove():
    row = int(input("choose a row number: "))
    # prompt the user separately for the row and column numbers
    col = int(input("choose a column number: "))
    return row, col  # then return that row and column instead of (0,0)


def hasBlanks(board):
    # search entire board for a blank, and return true if we find one, and false if we don't
    for rowNumber in range(0, 3):
        for colNumber in range(0, 3):
            if board[rowNumber][colNumber] == 0:
                return True
    return False


def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player_number = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        if markBoard(board, row, col, player_number) is True:
            player_number = player_number % 2 + 1  # switch player for next turn


main()