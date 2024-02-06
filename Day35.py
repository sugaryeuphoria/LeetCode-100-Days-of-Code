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
# Example Usage:
solution = Solution()
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

strs2 = [""]
print(solution.groupAnagrams(strs2))
# Output: [['']]

strs3 = ["a"]
print(solution.groupAnagrams(strs3))
# Output: [['a']]