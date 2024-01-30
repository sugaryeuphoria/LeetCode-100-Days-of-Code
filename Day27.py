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

        # Iterate through the characters in the string
        for end in range(len(s)):

         # Check if the character is repeated and its last occurrence is after the start index
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
        
        # Move the start index to the next position of the repeated character
                start = char_index_map[s[end]] + 1

        # Update the last index of the character
            char_index_map[s[end]] = end