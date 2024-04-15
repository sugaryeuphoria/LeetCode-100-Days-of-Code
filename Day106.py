"""
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so
that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""
class Solution(object):
    def sumNumbers(self, root):
         # Define a depth-first search helper function
        def dfs(node, path_sum):
            # If the current node is None, return 0
            if not node:
                return 0
            # Update the path sum by appending the current node's value
            path_sum = path_sum * 10 + node.val
            # If the current node is a leaf node, return the accumulated path sum
            if not node.left and not node.right:  # If leaf node
                return path_sum
            # Recursively explore the left and right subtrees
            left_sum = dfs(node.left, path_sum)
            right_sum = dfs(node.right, path_sum)

            # Return the sum of path sums from left and right subtrees
            return left_sum + right_sum