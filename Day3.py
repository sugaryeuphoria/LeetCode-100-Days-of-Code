class Solution(object):
    def romanToInt(self, s):
        roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_dictionary[s[i]] < roman_dictionary[s[i + 1]]:
                 result -= roman_dictionary[s[i]]
            else:
                result += roman_dictionary[s[i]]

        return result

# Example usage
solution = Solution()
#result added
result = solution.romanToInt("III")
print(result)  # Output: 3

    