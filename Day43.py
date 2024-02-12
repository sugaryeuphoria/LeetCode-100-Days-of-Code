"""
169. Majority Element
Easy

18125

566

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
# Class definition
class Solution:

# Method defintion 
    def majorityElement(self, nums: List[int]) -> int:
        # Count
        count = 0
  # Find the candidate majority element
        for num in nums:
# If condition added
         if count == 0:
                candidate = num
                count += 1 if num == candidate else -1
 
        # Validate if the candidate is the majority element
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        return candidate if count > len(nums) // 2 else -1
