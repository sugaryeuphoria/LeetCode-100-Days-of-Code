"""
2962. Count Subarrays Where Max Element Appears at Least K Times
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums
appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2
times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""
class Solution(object):
    def countSubarrays(self, nums, k):
        # Find the maximum number in the array.
        maxNum = max(nums)
        # Initialize variables to keep track of the count of subarrays and the current count of the maximum number.
        ans = 0
        count = 0
        # Initialize the left pointer of the sliding window.
        l = 0
        
        # Iterate through the array using a sliding window approach.
        for r, num in enumerate(nums):
            # Increase the count if the current number is equal to the maximum number.
            if num == maxNum:
                count += 1
            # Keep the window to include k - 1 occurrences of the maximum number.
            while count == k:
                # Shrink the window by moving the left pointer if the current number is equal to the maximum number.
                if nums[l] == maxNum:
                    count -= 1
                l += 1
            # If l > 0, nums[l:r+1] has k - 1 occurrences of the maximum number. For any
            # subarray nums[i:r+1], where i < l, it will have at least k occurrences of the
            # maximum number, since nums[l - 1] equals the maximum number.
            ans += l
        # Return the total count of subarrays meeting the condition.
        return ans

# Example usage:
solution = Solution()
nums1 = [1, 3, 2, 3, 3]
k1 = 2
print(solution.countSubarrays(nums1, k1))  # Output: 6

nums2 = [1, 4, 2, 1]
k2 = 3
print(solution.countSubarrays(nums2, k2))  # Output: 0
