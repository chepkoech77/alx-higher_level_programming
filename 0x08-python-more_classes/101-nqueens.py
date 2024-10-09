#!/usr/bin/python3
"""This module solves puzzle"""


import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    # Create an empty chessboard
    board = [[0] * N for _ in range(N)]

    def solve_util(board, row):
        # Base case: If all queens are placed, print the board
        if row == N:
            for i in range(N):
                for j in range(N):
                    print(board[i][j], end=' ')
                print()
            print()
            return

        # Check every column in the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row][col] = 1

                # Recur to place rest of the queens
                solve_util(board, row + 1)

                # Backtrack and try other positions
                board[row][col] = 0

    solve_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

