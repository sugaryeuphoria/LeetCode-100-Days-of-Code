"""
2000. Reverse Prefix of Word
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:

1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
"""
class Solution(object):
    def reversePrefix(self, word, ch):
        # Find the index of the first occurrence of ch
        index = word.find(ch)  
        if index != -1:
             # Reverse the substring from the beginning of the word up to index
            return word[:index + 1][::-1] + word[index + 1:]
        else:
             # ch does not exist in word, so return the original word
            return word  
        # Example usage:
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
print(solution.reversePrefix("xyxzxe", "z"))   # Output: "zxyxxe"
print(solution.reversePrefix("abcd", "z"))     # Output: "abcd"
