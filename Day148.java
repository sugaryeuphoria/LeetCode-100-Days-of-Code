/*523. Continuous Subarray Sum
 Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
 */
class Solution {
    // Method to check if the array has a subarray whose sum is a multiple of k
    public boolean checkSubarraySum(int[] nums, int k) {
        // Variable to store the prefix sum
        int prefix = 0;
        // Map to store the remainder of the prefix sum and the index where it occurred
        Map<Integer, Integer> prefixToIndex = new HashMap<>();
        // Initialize the map with 0 remainder at index -1 to handle edge cases
        prefixToIndex.put(0, -1);

        // Loop through each element in the array
        for (int i = 0; i < nums.length; ++i) {
            // Add the current element to the prefix sum
            prefix += nums[i];
            // If k is not 0, take the remainder of the prefix sum divided by k
            if (k != 0)
                prefix %= k;
            // Check if this remainder has been seen before
            if (prefixToIndex.containsKey(prefix)) {
                // If the previous occurrence of this remainder is more than one index ago,
                // return true
                if (i - prefixToIndex.get(prefix) > 1)
                    return true;
            } else {
                // If this remainder hasn't been seen before, add it to the map with the current
                // index
                prefixToIndex.put(prefix, i);
            }
        }

        // If no valid subarray is found, return false
        return false;
    }
}
