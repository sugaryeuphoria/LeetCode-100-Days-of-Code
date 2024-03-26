"""
41. First Missing Positive
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        # Move all non-positive integers to the end of the array
        # Keep track of the count of positive integers
        k = 0
        for i in range(n):
            if nums[i] > 0:
                nums[k] = nums[i]
                k += 1
                 # Traverse the positive integers, marking their presence by negating the value at their corresponding index
        for i in range(k):
            if abs(nums[i]) <= k:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
                 # Find the first positive integer which is not marked (positive), indicating the missing positive integer
        for i in range(k):
            if nums[i] > 0:
                return i + 1
             # If all integers from 1 to k are present, the missing integer is k + 1
        return k + 1