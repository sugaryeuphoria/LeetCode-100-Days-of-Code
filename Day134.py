"""
2597. The Number of Beautiful Subsets
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""
import collections

class Solution:
    def beautifulSubsets(self, nums, k):
        # Count the frequency of each element in nums
        count = collections.Counter(nums)
        # Create a dictionary to group elements by their modulo k values
        modToSubset = collections.defaultdict(set)
        # Populate the dictionary with elements grouped by their modulo k value
        for num in nums:
            modToSubset[num % k].add(num)
            # Initialize prevNum to -k to handle the first comparison correctly
        prevNum = -k
        # Initialize skip and pick to 0
        skip = 0
        pick = 0
        # Iterate over each subset (group of elements with the same modulo k value)
        for subset in modToSubset.values():
            # Sort the subset to handle elements in order
            for num in sorted(subset):
                # Calculate the number of non-empty subsets for the current number
                nonEmptyCount = 2**count[num] - 1
                # If the current number and the previous number are k apart
                if num - prevNum == k:
                    # Update skip and pick considering the restriction
                    skip, pick = skip + pick, nonEmptyCount * (1 + skip)
                else:
                    # Update skip and pick without restriction
                    skip, pick = skip + pick, nonEmptyCount * (1 + skip + pick)
                    # Update prevNum to the current number for the next iteration
                prevNum = num
                 # Return the total number of beautiful subsets
        return skip + pick