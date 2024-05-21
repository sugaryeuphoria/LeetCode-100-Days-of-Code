"""
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
class Solution(object):
    def subsets(self, nums):
        # This will hold all the subsets
        res = []
        def backtrack(start, path):
            # Add the current subset (path) to the result
            res.append(path[:])
            # Try including each element starting from 'start'
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recur with the next starting index
                backtrack(i + 1, path)
                # Backtrack: remove nums[i] from the current subset
                path.pop()
                 # Start backtracking from the first index with an empty path
        backtrack(0, [])
        
        return res