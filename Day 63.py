"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
class Solution(object):
    def sortedSquares(self, nums):
        # Length of the input array
        n = len(nums)
        # Initialize the result array with zeros
        result = [0] * n
         # Pointers for the two ends of the array
        left, right = 0, n - 1
        # Index to fill in the result array
        index = n - 1
        # Loop until the pointers meet or cross each other
        while left <= right:
              # Calculate the squares of the elements pointed by the pointers
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
             # Compare the squares of the elements
            if left_sq > right_sq:
                 # Fill in the result array with the square of the element pointed by the left pointer
                result[index] = left_sq