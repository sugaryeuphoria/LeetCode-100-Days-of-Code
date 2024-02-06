from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Initialize the queue with the root and its level
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if the current node is a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add the left child to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            
            # Add the right child to the queue
            if node.right:
                queue.append((node.right, depth + 1))
