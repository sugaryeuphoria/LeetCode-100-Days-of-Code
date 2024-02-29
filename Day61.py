"""1609. Even Odd Tree
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""
from collections import deque
class Solution(object):
    def isEvenOddTree(self, root):
        # Check if the root is None
        if not root:
            return False
         # Initialize a queue for level-order traversal
        queue = deque([root])

        # Initialize the level index
        level = 0

        # Perform level-order traversal
        while queue:
            # Get the number of nodes in the current level
            level_size = len(queue)

            # Initialize the previous node's value as None
            prev_value = None