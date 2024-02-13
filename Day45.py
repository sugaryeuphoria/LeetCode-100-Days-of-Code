"""
2108. Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
"""

# Define a class
class Solution:

      # Define a method to check if a string is a palindrome
    def isPalindrome(self, s: str) -> bool:
        # Check if the string is equal to its reverse
        return s == s[::-1]
         # Define a method to find the first palindrome in the list of words
    def firstPalindrome(self, words: List[str]) -> str:

         # Iterate through each word in the list
        for word in words:

             # Check if the current word is a palindrome using the isPalindrome method
            if self.isPalindrome(word):