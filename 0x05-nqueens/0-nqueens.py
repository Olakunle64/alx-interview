#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid"""
    for r in range(row):
        if (
            board[r][col] == 1 or
            (col - (row - r) >= 0 and board[r][col - (row - r)] == 1) or
            (col + (row - r) < len(board) and board[r][col + (row - r)] == 1)
        ):
            return False
    return True


def solve_nqueens(board, row, solutions):
    """Use backtracking to solve the N queens problem"""
    n = len(board)
    if row == n:
        solutions.append([
            [r, c] for r in range(n) for c in range(n) if board[r][c] == 1
        ])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0  # Backtrack


def nQueens(n):
    """Solve the N queens problem and return all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nQueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
