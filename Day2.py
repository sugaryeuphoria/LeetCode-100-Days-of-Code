#class declaration
class Solution(object):

    #Method definition
    def isPalindrome(self, x):

        #Converting number to string
        num_str = str(x)

        #return the reverse
        return num_str == num_str[::-1]