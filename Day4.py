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
            # Check if the index is within the length of the last string
            # and if the characters at the current index are the same in both strings
            if i < len(last_str) and first_str[i] == last_str[i]:
                # Append the common character to the common_prefix list
                common_prefix.append(first_str[i])
            else:
                # Break the loop if the characters are not the same
                break

        # Join the characters in the common_prefix list to form the final result
        return "".join(common_prefix)

