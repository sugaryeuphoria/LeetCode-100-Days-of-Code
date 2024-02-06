"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children."""
#import deque from collections
from collections import deque

# method and class definition
class Solution(object):
    def minDepth(self, root):

         if not root:
            return 0