#!/usr/bin/python3
"""Queen Chess challenge

"""

import sys

def printSolution(board, n):
    for row in range(n):
        print (board[row])
    print()

def isSafe(board, row, col, n):
    """ Found if a position is safe or atacked by other Queen
    Arguments:
    board: Position of other queens
    row: row  position to   analyze
    col: col position to analyze
    Return: True if position is safe for a new Queen
    """

    """ veriying the row on left side """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """ veriying upper diagonal on left side """
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    """ veriying upper diagonal on left side """
    for i,j in zip(range(row, n, 1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        return True

def solveNQUtil(board, col, n):
    """ Found if a queen was placed on the column
    Arguments:
    board: Position of other queens
    col: col position to analyze
    Return: True if all queens has been placed
            false if the queen cannot be placed in all the col
    """

    if col >= n:
        return True

    """ Iter by col tryng to place the Queen row by row"""
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if solveNQUtil(board, col+1, n) == True:
                return True
            board[i][col] = 0

    return False

def solveNQ(n):
    """ Starting in an empty board, the function look for an arrange
    of Queens complying the challenge"""

    board = [[0 for x in range(n)] for y in range(n)]
    if solveNQUtil(board, 0, n) == False:
        print("Solution does not exist")
        return False
    printSolution(board, n)
    return True

if len(sys.argv) is not 2:
    print("Usage: nqueens N")
    exit(1)
n = int(sys.argv[1])
print(n)
#if n is not int:
#    print("N must be a number")
#    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
solveNQ(n)
