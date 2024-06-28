"""
2285. Maximum Total Importance of Roads
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
