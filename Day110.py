"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]  # Define a function that takes a 2D grid of characters as input
        :rtype: int  # The function returns an integer representing the number of islands
        
        """
        def dfs(i, j):
            # DFS function to explore the grid starting from cell (i, j)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                # If the current cell is out of bounds or it's water ('0'), return
                return
            grid[i][j] = '0'  # Mark the current cell as visited
            # Explore adjacent cells in all four directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0  # Initialize a variable to count the number of islands
        for i in range(len(grid)):  # Iterate over rows of the grid
            for j in range(len(grid[0])):  # Iterate over columns of the grid
                if grid[i][j] == '1':  # If the current cell is land ('1')
                    count += 1  # Increment the island count
                    dfs(i, j)  # Explore the island using DFS
        return count  # Return the total number of islands
