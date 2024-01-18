#Length of Last Word
class Solution(object):
    #Method declaration
    def lengthOfLastWord(self, s):
       # Split the string into words
        words = s.split()
       # Check if there are any words
        if not words:
            return 0
       # Get the length of the last word
        last_word = words[-1]
        return len(last_word)
        
