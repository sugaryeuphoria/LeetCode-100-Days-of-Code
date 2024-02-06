#import default dictionary
from collections import defaultdict

# class and method definition
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
             # Sort the characters of the word to create a unique key for anagrams
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())
