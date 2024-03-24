"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""
class Solution(object):
    def findDuplicate(self, nums):
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[nums[0]]
        
        # Find the meeting point of slow and fast pointers
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Reset slow pointer to the beginning
        slow = 0
        
        # Move both pointers one step at a time until they meet
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # The meeting point is the duplicate number
        return slow