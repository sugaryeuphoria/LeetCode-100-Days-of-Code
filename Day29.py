#Class definition
class Solution:
    #Method definition
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of the tree rooted at 'node'
        def height(node):
         