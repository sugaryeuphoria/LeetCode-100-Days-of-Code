#Class definition
class TreeNode(object):
    #Method defintion
    def __init__(self, val=0, left=None, right=None):
            #Node Creation
            self.val = val
            self.left = left
            self.right = right
#Class Creation
class Solution(object):
    # maxDepth method creation
    def maxDepth(self, root):
        #Return statement
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
