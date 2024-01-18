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

      