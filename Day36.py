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
         
           
        queue = deque([(root, 1)])  # 
    
        while queue:
            node, depth = queue.popleft()

         # Check if the current node is a leaf node
            if not node.left and not node.right:
                return depth
            
              # Add the left child to the queue
            if node.left:
                queue.append((node.left, depth + 1))