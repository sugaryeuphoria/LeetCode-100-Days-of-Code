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

            # Check for palindromes of length 2
        for i in range(n - 1):  # Iterate through each index up to the second-to-last index.
             
            if s[i] == s[i + 1]:  # Check if adjacent characters are equal.
                    dp[i][i + 1] = True  # Mark substrings of length 2 as palindromes.
            count += 1  # Increment the count of palindromic substrings.
            # Check for palindromes of length greater than 2
        for length in range(3, n + 1):  # Iterate through possible lengths of substrings greater than 2.
              for i in range(n - length + 1):  # Iterate through each starting index of substrings.
                      j = i + length - 1  # Calculate the ending index of the substring.