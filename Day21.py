#Class created
class Solution(object):
    #Method definition
    def isSymmetric(self, root):
        # Helper function to check if two trees are mirrors
        def isMirror(left, right):
            # If both are empty, they are mirrors
            if not left and not right:
                return True
             # If one is empty and the other is not, they are not mirrors
            if not left or not right:
                return False
             # Check if the values are the same and their subtrees are mirrors
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
         # If the tree is empty, it is symmetric
        if not root:
            return True