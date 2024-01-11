class Solution(object):
    def isValid(self,s):
        #create an empty stack to keep a track of open brackets
        stack=[]
        
        #define a dictionary to store the mapping of brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}

      