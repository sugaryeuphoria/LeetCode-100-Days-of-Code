"""
1915. Number of Wonderful Substrings
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.
Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""
class Solution:
     # Method to calculate the number of wonderful substrings in a given string
    def wonderfulSubstrings(self, word: str) -> int:
        # Initialize the count of wonderful substrings to 0
        ans = 0
        # Initialize the binary prefix to 0
        prefix = 0  # the binary prefix
        # Initialize a list to store the count of each binary prefix
        count = [0] * 1024  # the binary prefix count
        # The count of the empty string is 1
        count[0] = 1  # the empty string ""
        # Loop through each character in the input word
        for c in word:
            # Update the binary prefix by toggling the bit corresponding to the current character
            prefix ^= 1 << (ord(c) - ord('a'))
            # Add the count of the current binary prefix to the total number of wonderful substrings
            ans += count[prefix]
            # Add the counts of all binary prefixes obtained by toggling one bit of the current prefix
            for i in range(10):
                ans += count[prefix ^ (1 << i)]
                 # Increment the count of the current binary prefix
            count[prefix] += 1
