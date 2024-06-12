/*
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 */

public class Day152 {
    public void sortColors(int[] nums) {
        // Initialize pointers for tracking positions of 0s, 1s, and 2s
        int zero = -1;
        int one = -1;
        int two = -1;
        // Iterate through each number in the input array
    for (final int num : nums)

    // If the number is 0, place 0 in its new position, then place 1 and 2 in their respective new positions
      if (num == 0) {
        nums[++two] = 2;  // Place 2 at the next position
        nums[++one] = 1;  // Place 1 at the next position
        nums[++zero] = 0; // Place 0 at the next position
      } 
    }

}
