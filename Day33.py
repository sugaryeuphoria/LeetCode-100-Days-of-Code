#Import default dictionary
from collections import defaultdict

#Class and method definition
class Solution(object):
    def firstUniqChar(self, s):

 # Let's use a defaultdict to count occurrences
        char_count = defaultdict(int)
