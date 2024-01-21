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