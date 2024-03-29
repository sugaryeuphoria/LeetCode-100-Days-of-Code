"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""
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
    #method declaration
    def isSameTree(self, p, q):
        # Base case: If both trees are empty, they are the same
        if not p and not q:
            return True
        
        # If one tree is empty and the other is not, they are different
        if not p or not q:
            return False
        
      # Check if the current nodes have the same value
        if p.val != q.val:
            return False

        # Check left and right branches only if not both nodes are None
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
# Create tree nodes using the class method
node1 = TreeNode.create(1)
node2 = TreeNode.create(2)
node3 = TreeNode.create(3)

# Build trees
tree1 = TreeNode.create(1, node2, node3)
tree2 = TreeNode.create(1, node2, node3)

# Create Solution object
solution = Solution()

# Check if trees are the same
result = solution.isSameTree(tree1, tree2)
print(result)  # Output: True
  
     
     