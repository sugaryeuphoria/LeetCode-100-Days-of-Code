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


# Alternate method
    #Class creation 
class TreeNode(object):
    #Overide class method
    @classmethod
    def create(cls, val=0, left=None, right=None):
        #Node creation
        node = cls()
        node.val = val
        node.left = left
        node.right = right
        return node
#Class definition
class Solution(object):
    #Method definition
    def maxDepth(self, root):
        
        def calculate_depth(node):
            if node is None:
                return 0
            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)
            return max(left_depth, right_depth) + 1

        return calculate_depth(root)

# Example usage:
# node = TreeNode.create(3, TreeNode.create(9), TreeNode.create(20, TreeNode.create(15), TreeNode.create(7)))
# solution = Solution()
# depth = solution.maxDepth(node)
# print(depth)
    