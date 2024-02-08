"""Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares
while 3 and 11 are not.
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9."""
# Class definition
class Solution(object):
    # Method definition
    def numSquares(self, n):

        # Generate a list of perfect squares less than or equal to n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        # Initialize a list to store the minimum number of perfect squares required for each number up to n
        dp = [float('inf')] * (n + 1)

         # Base case: 0 perfect squares required for 0
        dp[0] = 0

         # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):

             # Iterate through all perfect squares less than or equal to i
            for square in squares:

                 # If the current number is less than the square, break out of the loop
                if i < square:
                    break

                 # Update the minimum number of perfect squares required for the current number i
                dp[i] = min(dp[i], dp[i - square] + 1)