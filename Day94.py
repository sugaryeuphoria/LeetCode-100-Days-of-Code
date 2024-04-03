"""
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Define a recursive backtracking function
        def backtrack(i, j, k):
            # If we've matched all characters in the word, return True
            if k == len(word):
                return True
            # Check if the current cell is out of bounds or doesn't match the current character
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            # Temporarily mark the current cell as visited
            temp, board[i][j] = board[i][j], '/'
            # Recursively explore neighboring cells in all directions
            res = backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or \
                  backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)
            # Restore the original value of the current cell
            board[i][j] = temp
            return res
        
        # Iterate through each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If the backtracking function returns True, the word is found
                if backtrack(i, j, 0):
                    return True
        # If no match is found after exploring all cells, return False
        return False
