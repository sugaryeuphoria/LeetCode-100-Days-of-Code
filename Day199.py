"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping digits to their corresponding letters
        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        # This will hold the list of all combinations
        result = []
        # Helper function to perform backtracking
        def backtrack(index, current_combination):
            # If the current combination is the same length as digits, we have a full combination
            if index == len(digits):
                result.append("".join(current_combination))
                return
            # Get the current digit and its corresponding letters
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                # Add the letter and recurse with the next index
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                # Backtrack by removing the last added letter
                current_combination.pop()
        # Start the backtracking process
        backtrack(0, [])
        
        return result

        