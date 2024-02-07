""" Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits."""
#Import counter
from collections import Counter
# Class definition
class Solution(object):
# Method definition
    def frequencySort(self, s):
        # Count the frequency of each character
        count = Counter(s)
# Sort the characters based on their frequency in descending order
        sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))
         # Build the sorted string
        sorted_str = ''.join(char * freq for char, freq in sorted_chars)