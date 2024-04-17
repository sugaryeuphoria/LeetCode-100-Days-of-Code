class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node:
                return "|"
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                return ''.join(path[::-1])