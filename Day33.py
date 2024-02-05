"""Examples added:Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2"""
#Import default dictionary
from collections import defaultdict

#Class and method definition
class Solution(object):
    def firstUniqChar(self, s):

 # Let's use a defaultdict to count occurrences
        char_count = defaultdict(int)

 # First pass: Count occurrences
        for char in s:
            char_count[char] += 1

 # Second pass: Find the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i 

  # If no unique character is found, return -1
        return -1
                   