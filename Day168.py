"""
2285. Maximum Total Importance of Roads
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.
Return the maximum total importance of all roads possible after assigning the values optimally.
"""
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        # Step 1: Count the degrees
        degrees = defaultdict(int)
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1

        # Step 2: Sort cities by degree in descending order
        sorted_cities = sorted(degrees.keys(), key=lambda x: degrees[x], reverse=True)

        # Step 3: Assign values from n down to 1
        value_assignment = {}
        value = n
        for city in sorted_cities:
            value_assignment[city] = value
            value -= 1

        # If there are cities with no roads, assign them the remaining values
        for i in range(n):
            if i not in value_assignment:
                value_assignment[i] = value
                value -= 1

        # Step 4: Calculate the total importance
        total_importance = 0
        for a, b in roads:
            total_importance += value_assignment[a] + value_assignment[b]

        return total_importance
