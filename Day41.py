"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
class Solution(object):  # Define a class named Solution.
    def countSubstrings(self, s):  # Define a method named countSubstrings within the Solution class, which takes a string 's' as input.
        """
        :type s: str
        :rtype: int
        """
        n = len(s)  # Get the length of the input string.
        count = 0  # Initialize a variable 'count' to store the count of palindromic substrings.
        dp = [[False] * n for _ in range(n)]  # Initialize a 2D array 'dp' to store whether substrings are palindromes or not.

        # Single characters are palindrome by default
        for i in range(n):  # Iterate through each index of the string.
            dp[i][i] = True  # Mark single characters as palindromes.
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
                if s[i] == s[j] and dp[i + 1][j - 1]:  # Check if the characters at the ends are equal and the substring within them is a palindrome.
                    dp[i][j] = True  # Mark the current substring as a palindrome.
                    count += 1  # Increment the count of palindromic substrings.

        return count  # Return the total count of palindromic substrings.
