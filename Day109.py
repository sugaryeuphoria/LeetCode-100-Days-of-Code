"""
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one
island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected 
to the water around the island. One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""
class Solution(object):
    def islandPerimeter(self, grid):
        # Initialize perimeter variable to keep track of the total perimeter
        perimeter = 0
        # Iterate through each row in the grid
        for i in range(len(grid)):
            # Iterate through each column in the grid
            for j in range(len(grid[0])):
                 # Check if the current cell is land
                if grid[i][j] == 1:
                    # If the current cell is land, add 4 to the perimeter
                    perimeter += 4  # Each land cell contributes 4 edges to the perimeter
                    # Check if the neighboring cell to the top is also land
                    if i > 0 and grid[i - 1][j] == 1:
                        # If neighboring cell to the top is land, subtract 2 from the perimeter
                        perimeter -= 2  # Reduce perimeter by 2 if neighbor is land
                        # Check if the neighboring cell to the left is also land
                    if j > 0 and grid[i][j - 1] == 1:
                         # If neighboring cell to the left is land, subtract 2 from the perimeter
                        perimeter -= 2  # Reduce perimeter by 2 if neighbor is land
                         # Return the total perimeter of the island
        return perimeter
    