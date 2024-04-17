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