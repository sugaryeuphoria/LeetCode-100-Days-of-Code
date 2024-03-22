"""
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

The '.' character indicates empty cells.
Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
class Solution(object):
    def solveSudoku(self, board):
         # Function to solve the Sudoku puzzle
        self.solve(board)
        def solve(self, board):
              # Iterate through each cell of the board
        for row in range(9):
            for col in range(9):
                # Check if the cell is empty
                if board[row][col] == '.':
                    # Try placing digits from 1 to 9 in the cell
                    for digit in map(str, range(1, 10)):
                         # Check if the placement of the digit is valid
                        if self.is_valid(board, row, col, digit):
                             # Place the digit and recursively call the function
                            board[row][col] = digit
                            if self.solve(board):
                                return True
                            # Backtrack if no solution found
                            board[row][col] = '.'
                              # If no digit can be placed, return False
                    return False
                  # If all cells are filled, return True
        return True
    def is_valid(self, board, row, col, digit):
          # Check if the digit is valid according to Sudoku rules
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit or \
               board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
                return False
        return True
