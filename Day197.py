"""
2516. Take K of Each Character From Left and Right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
"""
from collections import Counter
class Solution(object):
    def takeCharacters(self, s, k):
        cnt = Counter(s)
        # Check if any character ('a', 'b', 'c') has less than 'k' occurrences
        if any(cnt[c] < k for c in "abc"):
            # Return -1 if it's impossible to take k of each character
            return -1  
        
        # Initialize the answer (window size) and left pointer 'j'
        ans = j = 0

        # Iterate over the string, with 'i' as the right pointer
        for i, c in enumerate(s):

            # Decrease the count of the current character at 'i'
            cnt[c] -= 1 

            # While the count of the current character is less than 'k', move the left pointer
            while cnt[c] < k:
                # Increment the count of character at left pointer 'j'
                cnt[s[j]] += 1
                # Move the left pointer to the right
                j += 1

                # Update the maximum length of the valid window
                ans = max(ans, i - j + 1)

                # Return the minimum length of string needed
                return len(s) - ans