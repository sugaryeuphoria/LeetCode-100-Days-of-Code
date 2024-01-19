"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator."""
class Solution(object):
    def mySqrt(self, x):
        
        # Handle base case
        if x == 0 or x == 1:
            return x

        # Binary search for the square root
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            # Check if mid is the square root
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        # Return the floor value of the square root
        return right
