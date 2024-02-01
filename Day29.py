#Class definition
class Solution:
    #Method definition
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of the tree rooted at 'node'
        def height(node):
           # Base case: If the node is None, the height is 0
            if not node:
                return 0
            
             # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
              # Check if the left or right subtree is unbalanced, or if the current subtree is unbalanced
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                 # If any of the above conditions are true, the subtree is unbalanced, return -1
                return -1
              # If the current subtree is balanced, return the height of the subtree
            return 1 + max(left_height, right_height)