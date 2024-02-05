#Class and method definition
class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s