/* 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
*/
class UnionFind {
    // Array to store the parent of each node
    private int[] p;
    // Array to store the size of each set
    private int[] size;
    // Number of disjoint sets
    public int cnt;

    public UnionFind(int n) {
        // Initialize parent array
        p = new int[n];
        // Initialize size array
        size = new int[n];
        for (int i = 0; i < n; ++i) {
            // Each node is its own parent initially
            p[i] = i;
            // Initial size of each set is 1
            size[i] = 1;
        }
        cnt = n; // Initially, there are 'n' disjoint sets
    }
    public int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]); // Path compression
        }
        return p[x]; // Return the root of the set containing 'x'
    }
    public boolean union(int a, int b) {
        int pa = find(a - 1), pb = find(b - 1); // Find roots of sets containing 'a' and 'b'
        if (pa == pb) {
            return false; // 'a' and 'b' are already in the same set
        }
        if (size[pa] > size[pb]) {
            p[pb] = pa; // Attach smaller tree under larger tree
            size[pa] += size[pb]; // Update the size of the set
        } else {
            p[pa] = pb; // Attach smaller tree under larger tree
            size[pb] += size[pa]; // Update the size of the set
        }
        --cnt; // Decrease the number of disjoint sets
        return true; // Union was successful
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        UnionFind ufa = new UnionFind(n); // Union-find for Alice
        UnionFind ufb = new UnionFind(n); // Union-find for Bob
        int ans = 0; // Counter for the number of removable edges
        for (var e : edges) {
            int t = e[0], u = e[1], v = e[2]; // Extract edge type and nodes
            if (t == 3) { // Type 3 edge
                if (ufa.union(u, v)) { // Try to union in Alice's union-find
                    ufb.union(u, v); // Also union in Bob's union-find
                } else {
                    ++ans; // Edge is redundant
                }
            }
        }
        for (var e : edges) {
            int t = e[0], u = e[1], v = e[2]; // Extract edge type and nodes
            if (t == 1 && !ufa.union(u, v)) { // Type 1 edge for Alice
                ++ans; // Edge is redundant
            }
            if (t == 2 && !ufb.union(u, v)) { // Type 2 edge for Bob
                ++ans; // Edge is redundant
            }
        }
        // Check if both Alice and Bob can traverse the graph
        return ufa.cnt == 1 && ufb.cnt == 1 ? ans : -1;
    }
}
