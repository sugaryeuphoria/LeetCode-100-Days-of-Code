class Solution:
    def maxPalindromesAfterOperations(self, words):
        word_lengths = []
        letter_counts = [0] * 26
        
        for word in words:
            word_lengths.append(len(word))
            for letter in word:
                letter_counts[ord(letter) - ord('a')] += 1
        
        can_make_palindrome = 0
        for count in letter_counts:
            can_make_palindrome += count // 2
        
        word_lengths.sort()
        max_palindromes = 0
        for length in word_lengths:
            needed = length // 2
            if can_make_palindrome >= needed:
                can_make_palindrome -= needed
                max_palindromes += 1
        
        return max_palindromes
