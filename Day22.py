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