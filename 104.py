"""
85.Maximal Rectangle
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1
 
Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
         # Check if the matrix is empty
        if not matrix:
            return 0
         # Function to calculate the largest rectangle area in histogram
        def maximalRectangleHistogram(heights):
            stack = []
            max_area = 0
            heights.append(0)  
            # Append a 0 to handle the case when heights end with non-zero elements
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]: