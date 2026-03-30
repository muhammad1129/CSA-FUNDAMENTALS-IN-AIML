def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all possible solutions.
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_util(board, 0, n, solutions)
    return solutions

def solve_util(board, col, n, solutions):
    """
    Recursive utility function to place queens using backtracking.
    """
    # Base case: If all queens are placed, add the current board to solutions
    if col >= n:
        solutions.append(["".join(row) for row in board])
        return

    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place the queen
            solve_util(board, col + 1, n, solutions)  # Recur for the next column
            board[row][col] = '.'  # Backtrack: Remove the queen if it doesn't lead to a solution

def is_safe(board, row, col, n):
    """
    Checks if it's safe to place a queen at board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    # Check lower diagonal on the left side
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1

    return True

# Example usage:
if __name__ == "__main__":
    n = 4  # For a 4x4 chessboard
    solutions = solve_n_queens(n)

    if solutions:
        print(f"Found {len(solutions)} solutions for N = {n}:")
        for i, sol in enumerate(solutions):
            print(f"Board {i+1}:")
            for r in sol:
                print(r)
            print("-" * (n * 2))
    else:
        print(f"No solutions found for N = {n}")