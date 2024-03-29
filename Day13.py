"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""
#Class Declaration
class Solution(object):
    #Method definition
    def plusOne(self, digits):
        # Iterate through the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
           # Increment the current digit
            digits[i] += 1
             # Check for carry
            if digits[i] < 10:
                return digits
            # If there is a carry, set the current digit to 0
            digits[i] = 0

            # If there is a carry after iterating through all digits, insert 1 at the beginning
            digits.insert(0, 1)
        
            return digits