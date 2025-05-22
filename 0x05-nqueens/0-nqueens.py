#!/usr/bin/python3
'''Solve N queens puzzle'''
import sys


def nqueens(row, board, solutions, n):
    '''Functions that solve the puzzle'''
    if row == n:
        solv = [[j, board[j]] for j in range(n)]
        solutions.append(solv)
        return
    for column in range(n):
        if all(board[i] != column and
               board[i] - i != column - row and
               board[i] + i != column + row for i in range(row)):
            board[row] = column
            nqueens(row + 1, board, solutions, n)


def main():
    '''main function'''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        return
    if n < 4:
        print(' N must be at least 4')
        return
    sol = []
    board = n * [-1]
    nqueens(0, board, sol, n)
    for solution in sol:
        print(solution)


if __name__ == '__main__':
    main()
