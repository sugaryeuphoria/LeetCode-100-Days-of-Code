"""
678. Valid Parenthesis String
Given a string s containing only three types of 
characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis 
'(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
class Solution(object):
    def checkValidString(self, s):
         # Initialize counts for minimum and maximum open parentheses
        min_open = max_open = 0
        # Iterate through each character in the string
        for char in s:
             # If the character is '(', increment both minimum and maximum counts
            if char == '(':
                min_open += 1
                max_open += 1
                # If the character is ')', decrement minimum count and decrement maximum count if possible
            elif char == ')':
                min_open = max(min_open - 1, 0)
                max_open -= 1
                # If maximum count becomes negative, it means ')' cannot be balanced, return False
                if max_open < 0:
                    return False
                 # If the character is '*', decrement minimum count and increment maximum count
            else:  # char == '*'
                min_open = max(min_open - 1, 0)
                max_open += 1
                 # Check if minimum count of open parentheses is 0, indicating a valid string
        return min_open == 0