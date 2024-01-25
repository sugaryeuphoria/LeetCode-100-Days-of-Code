#Class created
class Solution(object):
    #Method definition
    def longestPalindrome(self, s):
        #def another method
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
         # Base case: if the string has 1 or 0 characters, it's already a palindrome
        if len(s) <= 1:
            return s
         # Initialize the variable to store the longest palindrome
        longest_palindrome = ""
      