#Import
from collections import Counter  # Import Counter to efficiently count character frequencies.
#Class and method definition
class Solution(object):
    def minWindow(self, s, t):
        char_count_t = Counter(t)  # Count the frequencies of characters in string t.
        required_chars = len(char_count_t)  # Total unique characters required to form the window.

        left, right = 0, 0  # Pointers to define the current window.
        formed_chars = 0  # Count of unique characters formed in the current window.
         window_char_count = Counter()  # Counter to track character frequencies in the current window.