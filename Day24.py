#Class creation
class Solution:
    
    #Method declaration
    def findMedianSortedArrays(self, nums1, nums2):
        # Get lengths of both arrays
        m, n = len(nums1), len(nums2)

        #Ensure nums1 is the smaller array
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        # Set initial values for binary search
        i_min, i_max, half_len = 0, m, (m + n + 1) // 2

        while i_min <= i_max:

             # Perform binary search on nums1
            i = (i_min + i_max) // 2
            j = half_len - i

            # Check conditions for the binary search
            if i < m and nums2[j - 1] > nums1[i]:
               # Increase i, since i is too small
                i_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                 # Decrease i, since i is too large
                i_max = i - 1
            else:
                # i is perfect, calculate median
                max_left = max(nums1[i - 1] if i > 0 else float('-inf'), nums2[j - 1] if j > 0 else float('-inf'))
                if (m + n) % 2 == 1:
                    # Odd total length, return max_left as median
                    return float(max_left)