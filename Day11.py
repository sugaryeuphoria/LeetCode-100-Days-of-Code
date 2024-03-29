"""Search Insert Position:Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104"""
#Class definiton
class Solution(object):
    def searchInsert(self, nums, target):
    
        # Initialize variables
        low, high = 0, len(nums) - 1

         # Binary search algorithm
        while low <= high:
            mid = (low + high) //2

        # Check if target is at mid position
        if nums[mid] == target:
            return mid
        
         # Adjust search space based on target and nums[mid]
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

          
        # Target not found, return the position to insert
        return low
