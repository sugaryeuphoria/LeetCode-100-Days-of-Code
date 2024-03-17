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
        count = 0  # Initialize a variable to store the cumulative count of 0s and 1s
        for i, num in enumerate(nums):  # Iterate through each element and its index in the input list
            if num == 0:  # If the current element is 0
                count -= 1  # Decrement the cumulative count
            else:  # If the current element is 1
                count += 1  # Increment the cumulative count
            
            if count in hashmap:  # If the current cumulative count exists in the hashmap
                max_length = max(max_length, i - hashmap[count])  # Update the maximum length if needed
            else:  # If the current cumulative count does not exist in the hashmap
                hashmap[count] = i  # Add the current cumulative count and its index to the hashmap
        
        return max_length  # Return the maximum length of contiguous subarray