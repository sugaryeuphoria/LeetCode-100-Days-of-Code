"""
1219. Path with Maximum Gold
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
class Solution:
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Define directions: left, right, up, down
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        # Function to perform DFS to find maximum gold starting from a cell
        def dfs(row, col):
            # Check if out of grid or cell has no gold
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            # Save current cell's gold and set it to 0 to mark as visited
            gold = grid[row][col]
            grid[row][col] = 0
            
            # Recursively explore neighboring cells
            maxGold = 0
            for dr, dc in directions:
                maxGold = max(maxGold, dfs(row + dr, col + dc))
            
            # Restore gold value of current cell and return maximum gold found
            grid[row][col] = gold
            return gold + maxGold
        
        # Iterate over each cell to start DFS and find maximum gold
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, dfs(i, j))
        
        return maxGold
