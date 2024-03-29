"""
713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous
subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        # If k is less than or equal to 1, no subarray can have a product less than k.
        if k <= 1:
            return 0

        # Initialize variables to keep track of product, count of valid subarrays, and left pointer.
        product = 1  # Initialize product to 1, as we will be multiplying elements in the subarray.
        count = left = 0  # Initialize count and left pointer to 0.

        # Iterate through the nums list using right pointer.
        for right, num in enumerate(nums):
            # Update product by multiplying with the current element.
            product *= num
            
            # While product is greater than or equal to k, shrink the window from the left.
            while product >= k:
                # Divide product by the element at the left pointer and move the left pointer forward.
                product /= nums[left]
                left += 1
            
            # Add the count of valid subarrays ending at the current index (right) to the total count.
            count += right - left + 1

        # Return the total count of valid subarrays.
        return count
