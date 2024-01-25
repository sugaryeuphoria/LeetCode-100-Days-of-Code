class TreeNode:
    #Method declaration
    @classmethod
    def create(cls, val=0, left=None, right=None):
        #Node generation
        node = cls()
        node.val = val
        node.left = left
        node.right = right
        return node
#Solution class created
class Solution:
   