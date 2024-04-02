"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character,
but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
         # Create dictionaries to store mappings
        map_s_t = {}
        map_t_s = {}
        # Iterate through characters in s and t
        for char_s, char_t in zip(s, t):
             # If both characters are new, create mappings
            if (char_s not in map_s_t) and (char_t not in map_t_s):
                map_s_t[char_s] = char_t
                map_t_s[char_t] = char_s
                # If mappings don't match, return False
            elif map_s_t.get(char_s) != char_t or map_t_s.get(char_t) != char_s:
                return False
             # All mappings are valid, return True
        return True
