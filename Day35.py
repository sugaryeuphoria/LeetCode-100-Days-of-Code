#import default dictionary
from collections import defaultdict

# class and method definition
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs: