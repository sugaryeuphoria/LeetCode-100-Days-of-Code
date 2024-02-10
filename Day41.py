"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
class Solution(object):  # Define a class named Solution.
      def countSubstrings(self, s):  # Define a method named countSubstrings within the Solution class, which takes a string 's' as input.
              n = len(s)  # Get the length of the input string.
              count = 0 # Initialize a 2D array 'dp' to store whether substrings are palindromes or not.

                # Single characters are palindrome by default
      for i in range(n):  # Iterate through each index of the string.
              dp[i][i] = True  # Mark single characters as palindromes
               count += 1  # Increment the count of palindromic substrings.
