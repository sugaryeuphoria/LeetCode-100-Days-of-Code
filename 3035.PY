class Solution:
    def maxPalindromesAfterOperations(self, words):
        word_lengths = []
        letter_counts = [0] * 26
        
        for word in words:
            word_lengths.append(len(word))
            for letter in word:
                letter_counts[ord(letter) - ord('a')] += 1
        
      