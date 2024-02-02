"""An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits."""
#Class and method definition
class Solution(object):
    def sequentialDigits(self, low, high):
        # Initialize an empty list to store sequential digits in the given range

        result = []

        # Iterate through the digits 1 to 9
        for i in range(1, 10):  # Start from 1 to 9
            # Initialize the current number with the current digit
            num = num * 10 + j  # Add the next digit to the current number

            # Check if the current number is within the given range
            if low <= num <= high:
                    result.append(num)  # Add the current number to the result list

             # Break if the number goes beyond the high limit
            if num > high:  
                break

            return sorted(result)  # Return the sorted list of sequential digits