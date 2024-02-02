#Class and method definition
class Solution(object):
    def sequentialDigits(self, low, high):
        # Initialize an empty list to store sequential digits in the given range

        result = []

        # Iterate through the digits 1 to 9
        for i in range(1, 10):  # Start from 1 to 9