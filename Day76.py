"""
525. Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution(object):
    def findMaxLength(self, nums):
        hashmap = {0: -1}  # Initialize a hashmap to store the cumulative count of 0s and 1s and their indices
        max_length = 0  # Initialize a variable to store the maximum length of contiguous subarray
