"""
1248. Count Number of Nice Subarrays
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
class Solution(object):
    def numberOfSubarrays(self, nums, k):
         # This will store the count of prefix sums
        prefix_counts = {0: 1}
        current_prefix_sum = 0
        nice_subarrays_count = 0
        
        for num in nums:
             # Increment the prefix sum if the number is odd
            current_prefix_sum += num % 2
            # If (current_prefix_sum - k) is in prefix_counts, it means there is a subarray
            # ending at the current element which has exactly k odd numbers
            if (current_prefix_sum - k) in prefix_counts:
                nice_subarrays_count += prefix_counts[current_prefix_sum - k]
                 # Update the prefix_counts map
            if current_prefix_sum in prefix_counts:
                prefix_counts[current_prefix_sum] += 1
            else:
                prefix_counts[current_prefix_sum] = 1
        
        return nice_subarrays_count
# Example usage:
solution = Solution()
print(solution.numberOfSubarrays([1,1,2,1,1], 3))  # Output: 2
