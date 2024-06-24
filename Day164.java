/*
 995. Minimum Number of K Consecutive Bit Flips
 You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length
 */

 class Solution {
    public int minKBitFlips(int[] nums, int k) {
        // Get the length of the input array
        int n = nums.length;
        // Initialize an array to track the difference array for flips
        int[] d = new int[n + 1];
        // ans keeps the count of flips, s is the cumulative sum of flips
        int ans = 0, s = 0;
        // Iterate through each element in nums
        for (int i = 0; i < n; ++i) {
            // Add the current flip effect to s
            s += d[i];
            // Check if the current bit needs to be flipped
            if (nums[i] % 2 == s % 2) {
                // If flipping k bits starting from i exceeds array length, return -1
                if (i + k > n) {
                    return -1;
                }
                // Mark the start of a flip at position i
                ++d[i];
                // Mark the end of a flip at position i + k
                --d[i + k];
                // Update the cumulative sum to reflect the new flip
                ++s;
                // Increment the flip count
                ++ans;

    }
}