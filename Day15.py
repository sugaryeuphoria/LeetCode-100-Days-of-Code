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
