"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range
[1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
class Solution(object):
    def findDuplicates(self, nums):
        # Initialize a list to store duplicate numbers
        duplicates = [] 
        # Iterate through each number in the input list
        for num in nums:
            # Get the index corresponding to the absolute value of the current number
            index = abs(num) - 1
            # Check if the number at the calculated index is negative
            if nums[index] < 0:
                # If it's negative, the number has appeared before, so add it to the duplicates list
                duplicates.append(index + 1)
                # Mark the number at the calculated index as negative
                nums[index] = -nums[index]