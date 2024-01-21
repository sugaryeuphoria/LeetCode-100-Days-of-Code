""" You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
#Class definition
class Solution(object):
    #Method definition
    def climbStairs(self, n):
        # Base cases for n = 1 and n = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize variables for the two previous steps
        prev1 = 1
        prev2 = 2
        
     # Iterate from the third step to the nth step
        for i in range(3, n + 1):
            # Calculate the current step by summing the previous two steps
            current = prev1 + prev2
             # Update the previous steps for the next iteration
            prev1 = prev2
            prev2 = current
             # The final result is the number of distinct ways to reach the top
        return prev2