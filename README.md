# CSA2001-FUNDAMENTALS-IN-AIML
# ♛ N-Queens Problem Solver

A Python program that finds **all valid solutions** to the classic N-Queens problem
using recursive backtracking. Given any board size N, it places N queens on an
N×N chessboard such that no two queens can attack each other.

---

## What is the N-Queens Problem?

In chess, a **queen** is the most powerful piece — she can attack any square in
the same row, column, or diagonal. The N-Queens problem asks:

> *"Can you place N queens on an N×N chessboard so that none of them threatens
> any other?"*

For example, on a **4×4 board**, there are exactly **2 valid solutions**:
```
Solution 1:        Solution 2:
. Q . .            . . Q .
. . . Q            Q . . .
Q . . .            . . . Q
. . Q .            . Q . .
```

This problem is a classic exercise in **constraint satisfaction** and
**backtracking algorithms**, widely studied in computer science and AI.

---

## How It Works

The program uses a technique called **recursive backtracking**:

1. Queens are placed **one column at a time**, from left to right.
2. For each column, the program tries placing a queen in every row.
3. Before placing, it checks if the position is **safe** — no queen already
   placed can attack it from the same row, upper diagonal, or lower diagonal.
4. If the position is safe, it places the queen and moves to the next column.
5. If no row is safe in a column, it **backtracks** — removes the last queen
   and tries a different row in the previous column.
6. This continues until all columns are filled (a solution is found) or all
   possibilities are exhausted.

### Functions at a Glance

| Function | What It Does |
|---|---|
| `solve_n_queens(n)` | Entry point. Sets up the board and starts the search. |
| `solve_util(board, col, n, solutions)` | Recursive engine. Tries all placements column by column. |
| `is_safe(board, row, col, n)` | Checks whether placing a queen at (row, col) is conflict-free. |

---

## Requirements

- **Python 3.6 or higher**
- No external libraries required — uses only Python built-ins.

To check your Python version, run:
```bash
python3 --version
```

---

## Setup

### Step 1 — Clone or Download the Repository

If you have Git installed:
```bash
git clone https://github.com/your-username/digital-literacy-project.git
cd digital-literacy-project
```

Or simply **download the ZIP** from the green *Code* button on GitHub,
extract it, and open a terminal inside the folder.

### Step 2 — Navigate to the File

The program is a single file with no dependencies, so no installation is needed.
Just make sure you are in the correct directory:
```bash
cd digital-literacy-project   # or wherever nqueen.py is saved
```

---

## Usage

### Run with Default Settings (N = 4)

The file is pre-configured to run on a **4×4 board**:
```bash
python3 nqueen.py
```

**Expected output:**
```
Found 2 solutions for N = 4:
Board 1:
.Q..
...Q
Q...
..Q.
--------
Board 2:
..Q.
Q...
...Q
.Q..
--------
```

Each row of dots and Q's represents one row of the chessboard.
`Q` = queen placed, `.` = empty square.

---

### Change the Board Size

Open `nqueen.py` in any text editor and find this line near the bottom:
```python
n = 4  # For a 4x4 chessboard
```

Change `4` to any positive integer. For example, to solve for an **8×8 board**:
```python
n = 8  # For an 8x8 chessboard
```

Save the file and run it again:
```bash
python3 nqueen.py
```

> ⚠️ **Note:** For large values of N (above 12), the program may take a long
> time to run because the number of possibilities grows extremely fast.
> Start with small values like 4, 5, 6, or 8 to see quick results.

---

### Use It in Your Own Python Code

You can also import the solver into another Python script:
```python
from nqueen import solve_n_queens

solutions = solve_n_queens(6)
print(f"Total solutions for N=6: {len(solutions)}")

# Print the first solution
for row in solutions[0]:
    print(row)
```

---

## Sample Results by Board Size

| Board Size (N) | Number of Solutions |
|:-:|:-:|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |
| 10 | 724 |

---

## Project Structure
```
digital-literacy-project/
│
├── nqueen.py               ← Main program file
├── README.md               ← You are here
└── ...                     ← Other project files
```

---

## Key Concepts You Will Learn from This Code

- **Backtracking** — How to explore all possibilities and undo bad choices.
- **Recursion** — Solving a problem by breaking it into smaller identical steps.
- **Constraint Checking** — Validating conditions before committing to a choice.
- **2D Lists in Python** — Representing and manipulating a grid.

---

## Author

**Mohd Ali Siddiqui**
Registration No. — 25BAI10030
Branch — B.Tech CSE (Artificial Intelligence & Machine Learning)
VIT Bhopal University | Academic Year 2025–26

---

## License

This project is submitted as part of the **CSA2001 FUNDAMENTALS OF AIML** course
at VIT Bhopal University. Free to use for learning purposes.
