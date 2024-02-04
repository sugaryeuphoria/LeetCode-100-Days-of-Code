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
        min_len = float('inf')  # Initialize the minimum window length to positive infinity.
        min_window = ""  # Variable to store the minimum window substring.
        while right < len(s):
              # Expand the window and update character count
            window_char_count[s[right]] += 1
            if window_char_count[s[right]] == char_count_t[s[right]]:
                formed_chars += 1

             # Check if all characters from t are present in the current window
            while formed_chars == required_chars:
                # Update the minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
