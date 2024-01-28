#Class definition
class Solution(object):
   #Method definition
   def isMatch(self, s, p):
       # Create a memoization table to store intermediate results
        memo = {}
        def dp(i, j):
             # Check if the result is already memoized
            if (i, j) in memo:
                return memo[(i, j)]
             # Base case: if pattern is empty, return whether string is also empty
            if j == len(p):
                ans = i == len(s)
            else:
                # Check if the first characters match or if there is a '.' in the pattern
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                # Check for '*' in the pattern
                if j + 1 < len(p) and p[j + 1] == '*':

                 # Two options: 1. Ignore the '*' and move to the next character in the pattern
                    #              2. Keep the '*' and try to match the remaining string
                    ans = (dp(i, j + 2) or
                           (first_match and dp(i + 1, j)))
                else:
                    # If no '*', simply move to the next characters in both string and pattern
                    ans = first_match and dp(i + 1, j + 1)

                 # Memoize the result and return
                memo[(i, j)] = ans
                return ans

                return dp(0, 0)
            
# Example usage
sol = Solution()
print(sol.isMatch("aa", "a"))    # Output: False
print(sol.isMatch("aa", "a*"))   # Output: True
print(sol.isMatch("ab", ".*"))   # Output: True