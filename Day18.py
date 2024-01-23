#Class Declaration
class Solution(object):
    #Method Declaration
    def merge(self, nums1, m, nums2, n):

        # Initialize pointers for nums1 and nums2
        i = m - 1
        j = n - 1

        # Initialize pointer for the end of nums1
        k = m + n - 1

        # Merge from the end to the beginning
        while i >= 0 and j >= 0:
             # Compare elements from both arrays and place the larger one at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1