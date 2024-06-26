"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of 
the last word in the string.A word is a maximal substring consisting
of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        # Trim trailing spaces
        # Remove any trailing spaces at the end of the string
        s = s.rstrip()  
        # Initialize the length of the last word to 0
        length = 0 
        # Iterate through the string from the end towards the beginning
        for i in range(len(s) - 1, -1, -1):
            # If a space is encountered, it's the end of the last word
            if s[i] == ' ':
                 break  # Exit the loop
             # Increment the length for each non-space character encountered
            length += 1
             # Return the length of the last word
            return length
        
        # Test cases
sol = Solution()  # Create an instance of the Solution class
print(sol.lengthOfLastWord("Hello World"))  # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6

