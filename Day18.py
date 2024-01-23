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