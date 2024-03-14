"""
930. Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""
from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        # Initialize the answer variable to store the count of subarrays
        ans = 0
        # Initialize the prefix sum variable
        prefix = 0
        # Create a defaultdict to store the count of occurrences of each prefix sum
        count = defaultdict(int)
        # Initialize the count of prefix sum 0 to 1, as it is the starting point
        count[0] = 1

        # Iterate through each number in the nums array
        for num in nums:
            # Update the prefix sum
            prefix += num
            # Calculate the key for the desired sum by subtracting the goal from the prefix sum
            key = prefix - goal
            # Add the count of subarrays with the desired sum to the answer
            ans += count[key]
            # Increment the count of occurrences of the current prefix sum
            count[prefix] += 1

        # Return the total count of subarrays with the desired sum
        return ans

