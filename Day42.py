"""
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
"""
class Solution(object):  # Define a class named Solution.
     def cherryPickup(self, grid):  # Define a method named cherryPickup within the Solution class, which takes a grid as input.
           rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid.
           dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]  # Initialize a 3D DP array to store the maximum cherries collected at each position for both robots.
 def helper(r1, c1, c2):  # Define a recursive helper function to compute the maximum cherries that can be collected from a given state (r1, c1, c2).
       if r1 == rows:  # Base case: If the first robot reaches the bottom row, return 0 cherries.
              return 0
            if dp[r1][c1][c2] != -1:  # If the result for the current state has already been computed, return it.
              return dp[r1][c1][c2]

            cherries = grid[r1][c1]  # Cherries collected by the first robot at position (r1, c1).
       
       