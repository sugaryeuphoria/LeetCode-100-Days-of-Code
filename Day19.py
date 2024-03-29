""" 
Given the root of a binary tree, return the inorder traversal of its nodes' values.Day20.py

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Class definiton
class Solution(object):
    #Method definiton
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
         
            # Traverse the left subtree
            traverse(node.left)
            
            # Visit the current node (append its value to the result list)
            result.append(node.val)
            
            # Traverse the right subtree
            traverse(node.right)
        
        # Start the traversal from the root
        traverse(root)
        
        # Return the final result
        return result 
