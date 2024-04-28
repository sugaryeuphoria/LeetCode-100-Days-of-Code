"""
834. Sum of Distances in Tree

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""
class Solution(object):
    def sumOfDistancesInTree(self, n, edges):

         # Build adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

             # Arrays to store the answer and subtree sizes
        ans = [0] * n
        subtree_sizes = [0] * n

        # First DFS to compute subtree sizes and sum of distances
        def dfs1(node, parent):
            subtree_sizes[node] = 1
            for child in adj_list[node]:
                if child != parent:
                    dfs1(child, node)
                    subtree_sizes[node] += subtree_sizes[child]
                    ans[node] += ans[child] + subtree_sizes[child]
        # Second DFS to update answers
        def dfs2(node, parent):
            for child in adj_list[node]:
                if child != parent:
                    ans[child] = ans[node] - subtree_sizes[child] + (n - subtree_sizes[child])
                    dfs2(child, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
    
    