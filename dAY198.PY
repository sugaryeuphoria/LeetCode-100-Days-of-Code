"""
16. 3Sum Closest
Medium

10664

579

Add to List

Share
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0). 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array
        nums.sort()
        # Initialize with a large value
        closest_sum = float('inf')
        # Iterate over the array, treating nums[i] as the first element of the triplet
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                # Calculate the current sum of the triplet
                current_sum = nums[i] + nums[left] + nums[right]

                # Check if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                    # Move the pointers based on the comparison of current_sum and target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
