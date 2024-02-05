#Class and method definition
class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s
        
         # Initialize an empty list of lists to represent the rows
        rows = [''] * min(numRows, len(s))
        index, step = 0, 1

        #Initialize an empty list of lists to represent the rows
        rows = [''] * min(numRows, len(s))
        index, step = 0, 1

         # Iterate through each character in s
        for char in s: