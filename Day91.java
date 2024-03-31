/*
2444. Count Subarrays With Fixed Bounds
You are given an integer array nums and two integers minK and maxK.
A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:
2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
 */
class Day91 {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        // Variable to store the count of subarrays
        long ans = 0;
        // Pointer to track the last index where nums[i] is outside the range [minK, maxK]
        int j = -1;
        // Pointer to track the last index where nums[i] is equal to minK
        int prevMinKIndex = -1;
        // Pointer to track the last index where nums[i] is equal to maxK
        int prevMaxKIndex = -1;
        // Iterate through the array nums
    for (int i = 0; i < nums.length; ++i) {
        // If nums[i] is outside the range [minK, maxK], update j to the current index i
        if (nums[i] < minK || nums[i] > maxK)
j = i;
    }
}