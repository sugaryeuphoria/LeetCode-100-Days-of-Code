class Solution(object):
    def isValid(self,s):
        #create an empty stack to keep a track of open brackets
        stack=[]
        
        #define a dictionary to store the mapping of brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}

      # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_mapping:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'

             