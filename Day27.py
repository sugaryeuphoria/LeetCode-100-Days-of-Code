"""Given a string s, find the length of the longest substring without repeating characters.
Also appeared in the LeetCode contest
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
         # Map to store the last index of each character
        char_index_map = {}