"""Add Binary
Easy
9087
921
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
"""
class Solution(object):
    def addBinary(self, a, b):
        # Initialize variables to store the result and carry
        result = ""
        carry = 0

        # Iterate through the binary strings from right to left
        i, j = len(a) - 1, len(b) - 1

        # Continue until both binary strings are exhausted
        while i >= 0 or j >= 0:
            # Get the current bits from each binary string, default to 0 if exhausted
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            current_sum = bit_a + bit_b + carry
            carry = current_sum // 2
            current_sum %= 2

            # Prepend the current sum to the result
            result = str(current_sum) + result

            # Move to the next bit in each binary string
            i -= 1
            j -= 1

        # If there is a carry after iterating through all bits, prepend it to the result
            if carry > 0:
                result = str(carry) + result

            return result
