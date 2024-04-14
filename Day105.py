"""
404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Define a recursive function for depth-first search (DFS)
        def dfs(node, is_left):
            # If node is None, return 0
            if not node:
                return 0
            # If the node has no children and is a left child, return its value
            if not node.left and not node.right and is_left:
                return node.val
            # Recursively traverse left and right subtrees, updating is_left accordingly
            return dfs(node.left, True) + dfs(node.right, False)
        
        # Start DFS from the root with is_left initially set to False
        return dfs(root, False)
