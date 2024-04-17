class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node:
                return "|"