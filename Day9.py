#Class creation
class Solution(object):
    #Method definition
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
       # Check if needle is an empty string
        if not needle:
            return 0

      # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
      