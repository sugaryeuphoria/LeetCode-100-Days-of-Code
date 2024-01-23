# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Initialize the result list
        result = []
        
        # Helper function for recursive traversal
        def traverse(node):
            # Base case: if the node is None, return
            if not node:
                return
            
