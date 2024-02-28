"""
513. Find Bottom Left Tree Value
Given the root of a binary tree, return the leftmost value in the last row of the tree.
Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
# import deque
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Class and method definition
class Solution(object):
    def findBottomLeftValue(self, root):
        # Check if the root is None
        if not root:
            return None
         # Perform level-order traversal using a queue
        queue = deque([root])
         # Initialize the leftmost value as None
        leftmost_value = None
        while queue:

             # Get the size of the current level
            level_size = len(queue)

            # Iterate over all nodes in the current level
            for i in range(level_size):

                # Pop the node from the left of the queue
                node = queue.popleft()