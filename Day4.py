#lass created
class Solution(object):
     # Define a method named longestCommonPrefix that takes a list of strings as input
    def longestCommonPrefix(self, strs):
        # Check if the list of strings is empty
        if not strs:
            return ""

        # Sort the list of strings lexicographically
        strs.sort()

        # Get the first and last strings after sorting
        first_str, last_str = strs[0], strs[-1]

        # Initialize an empty list to store the common prefix characters
        common_prefix = []

        # Iterate through the characters of the first string
        for i in range(len(first_str)):
           
       