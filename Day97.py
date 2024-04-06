"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions
 ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""
class Solution(object):
    # Define a class Solution
    def maxDepth(self, s):
        # Define a method maxDepth that takes a string s as input
          # Initialize variables to track maximum depth and current depth
        max_depth = 0
        current_depth = 0
         # Iterate through each character in the string
        for char in s:
             # If the character is an opening parenthesis, increase the current depth
            if char == '(':
                current_depth += 1
                 # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
                # If the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                current_depth -= 1
                # Return the maximum depth encountered
        return max_depth