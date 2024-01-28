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