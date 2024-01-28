#Class definition
class Solution(object):
   #Method definition
   def isMatch(self, s, p):
       # Create a memoization table to store intermediate results
        memo = {}
        def dp(i, j):