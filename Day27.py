"""Given a string s, find the length of the longest substring without repeating characters.
Also appeared in the LeetCode contest
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
         # Map to store the last index of each character
        char_index_map = {}

        # Starting index of the current substring
        start = 0

        # Maximum length of substring without repeating characters
        max_length = 0