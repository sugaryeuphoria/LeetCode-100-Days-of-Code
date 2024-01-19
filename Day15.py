#Class definition
class Solution(object):
    #Method definition
    def mySqrt(self, x):
    
        # Handle base case
        if x == 0 or x == 1:
            return x
  # Binary search for the square root
        left, right = 0, x
       