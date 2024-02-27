"""543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Method and class definition
class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Initialize maximum diameter variable
        self.max_diameter = 0

         # Define a recursive function to calculate the depth of each node
        def depth(node):

             # Base case: if node is None, return 0
            if not node:
                return 0
            
             # Recursively calculate the depth of left subtree
            left_depth = depth(node.left)