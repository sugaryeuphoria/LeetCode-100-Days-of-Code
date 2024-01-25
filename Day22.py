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
         # Iterate through each character in the string
        for i in range(len(s)):
             # Check for odd-length palindromes with center at i
            palindrome_odd = expand_around_center(i, i)
            len_odd = len(palindrome_odd)

            # Update longest_palindrome if a longer palindrome is found
            if len_odd > len(longest_palindrome):
                longest_palindrome = palindrome_odd
            # Check for even-length palindromes with centers at i and i+1
            palindrome_even = expand_around_center(i, i + 1)
            len_even = len(palindrome_even)
      