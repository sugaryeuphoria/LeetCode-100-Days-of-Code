"""
2441. Largest Positive Integer That Exists With Its Negative
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
"""
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]  # Input parameter: list of integers
        :rtype: int  # Return type: integer
        """
        # Create a set of unique integers from the input list
        unique_nums = set(nums)
        # Initialize the maximum value of k to -1
        max_k = -1  
        # Iterate through each number in the input list
        for num in nums:  
            # If the negative of the current number exists in the set
            if -num in unique_nums:  
                # Update the maximum value of k encountered so far
                max_k = max(max_k, abs(num))  
                # Return the maximum value of k found, or -1 if none exists
        return max_k if max_k != -1 else -1  
