"""
992. Subarrays with K Different Integers
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        # Define a helper function to calculate the number of subarrays
        # with at most k distinct elements.
        def atMostK(nums, k):
            # Initialize a dictionary to keep track of the frequency of each element.
            freq = {}
            # Initialize a variable to count the number of distinct elements.
            count = 0
            # Initialize the variable to store the result.
            result = 0
             # Iterate over the array with the right pointer.
            for right in range(len(nums)):
                 # Update the frequency of the current element.
                freq[nums[right]] = freq.get(nums[right], 0) + 1
                 # If the frequency becomes 1, increment the count of distinct elements.
                if freq[nums[right]] == 1:
                    count += 1
                # If the count of distinct elements exceeds k, move the left pointer
                # forward and update the frequency and count accordingly.
                while count > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        count -= 1
                    left += 1
                     # Update the result by the difference in right and left pointers.
                result += right - left + 1
                # Return the result.
            return result
        # Return the difference between the number of subarrays with at most k
        # distinct elements and the number of subarrays with at most (k - 1) distinct elements.
        return atMostK(nums, k) - atMostK(nums, k - 1)
    # Example usage:
solution = Solution()
print(solution.subarraysWithKDistinct([1,2,1,2,3], 2))  # Output: 7
print(solution.subarraysWithKDistinct([1,2,1,3,4], 3))  # Output: 3

