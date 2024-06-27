"""
1791. Find Center of Star Graph
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Check the first two edges
        edge1 = edges[0]
        edge2 = edges[1]
        
        # The center node must appear in both edges
        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            return edge1[0]
        else:
            return edge1[1]
