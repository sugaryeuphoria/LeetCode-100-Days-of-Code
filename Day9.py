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
        #Inside the loop, it checks if the substring of haystack (starting from the current index i and having the same length as needle) is equal to needle. 
        
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # Return -1 if needle is not found
        return -1
