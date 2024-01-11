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

                # Check if the popped element matches the corresponding open bracket
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # If it's an open bracket, push it onto the stack
                stack.append(char)

        # The string is valid if the stack is empty at the end
        return not stack

# Example usage:
