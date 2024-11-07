#!/usr/bin/python3
import sys

def print_solution(solution):
    """Print the board solution in the specified format."""
    print([[i, col] for i, col in enumerate(solution)])

def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe from attacks."""
    for r, c in enumerate(solution[:row]):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n, row, solution, results):
    """Use backtracking to find all solutions for placing n queens on the board."""
    if row == n:
        results.append(solution[:])
        return
    for col in range(n):
        if is_safe(solution, row, col):
            solution[row] = col
            solve_nqueens(n, row + 1, solution, results)
            solution[row] = -1

def nqueens(n):
    """Find and print all solutions for the N queens problem."""
    solution = [-1] * n
    results = []
    solve_nqueens(n, 0, solution, results)
    for res in results:
        print_solution(res)

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

    nqueens(N)
