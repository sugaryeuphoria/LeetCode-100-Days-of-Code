"""
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
class TrieNode:
    def __init__(self):
        # Initialize the children list with 26 None values (for each letter a-z)
        self.children = [None] * 26
        # Initialize the word attribute to None
        self.word = None
class Solution:
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()

    def replaceWords(self, dictionary, sentence):
        # Insert each word from the dictionary into the Trie
        for word in dictionary:
            self.insert(word)

        # List to store the resulting words
        ans = []
        # Split the sentence into individual words
        words = sentence.split()

        # For each word in the sentence, search for its replacement
        for word in words:
            ans.append(self.search(word))

        # Join the words back into a single string and return
        return ' '.join(ans)
    def insert(self, word):
        # Start from the root of the Trie
        node = self.root
        # For each character in the word
        for c in word:
            # Calculate the index for the character
            i = ord(c) - ord('a')
            # If the corresponding child node doesn't exist, create it
            if node.children[i] is None:
                node.children[i] = TrieNode()
            # Move to the next node
            node = node.children[i]
        # Mark the end of the word
        node.word = word

        def search(self, word):
            # Start from the root of the Trie
            node = self.root
            # For each character in the word
            for c in word:
                # If a word is found, return it
                if node.word:
                    return node.word
                # Calculate the index for the character
                i = ord(c) - ord('a')
                # If the corresponding child node doesn't exist, return the original word
                if node.children[i] is None:
                    return word
                # Move to the next node
                node = node.children[i]
            # If no replacement is found, return the original word
            return word