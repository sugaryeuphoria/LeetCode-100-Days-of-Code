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
            heights.append(0)  # Append a 0 to handle the case when heights end with non-zero elements
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    # Pop the stack and calculate the rectangle area
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area

        # Get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        # Initialize the heights array to store the histogram heights
        heights = [0] * cols
        # Initialize the maximum rectangle area
        max_area = 0

        # Iterate through each row in the matrix
        for row in matrix:
            # Update the heights array based on the current row
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            # Calculate the maximum rectangle area using the histogram heights
            max_area = max(max_area, maximalRectangleHistogram(heights))

        return max_area
