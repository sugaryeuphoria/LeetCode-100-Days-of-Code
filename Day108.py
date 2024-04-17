"""
988. Smallest String Starting From Leaf
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
As a reminder, any shorter prefix of a string is lexicographically smaller.
For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""

class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node:
                return "|"
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                return ''.join(path[::-1])
            left_path = dfs(node.left, path)
            right_path = dfs(node.right, path)
            smallest_path = min(left_path, right_path)
            path.pop()
            return smallest_path
        return dfs(root, [])