#Class definition
class Solution(object):
   #Method definition
   def isMatch(self, s, p):
       # Create a memoization table to store intermediate results
        memo = {}
        def dp(i, j):
             # Check if the result is already memoized
            if (i, j) in memo:
                return memo[(i, j)]
             # Base case: if pattern is empty, return whether string is also empty
            if j == len(p):
                ans = i == len(s)
            else: