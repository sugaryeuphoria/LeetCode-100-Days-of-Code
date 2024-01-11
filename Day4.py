#lass created
class Solution(object):
     # Define a method named longestCommonPrefix that takes a list of strings as input
    def longestCommonPrefix(self, strs):
        # Check if the list of strings is empty
        if not strs:
            return ""

        # Sort the list of strings lexicographically
        strs.sort()

       