"""
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 
"""
class Solution(object):
    def intersection(self, nums1, nums2):
         # Convert the arrays to sets
        set1 = set(nums1)  # Convert nums1 to a set
        set2 = set(nums2)  # Convert nums2 to a set

        # Find the intersection of the two sets
        intersection_set = set1.intersection(set2)  # Find the common elements

         # Convert the intersection set back to a list
        intersection_list = list(intersection_set)  # Convert set to list

        return intersection_list  # Return the list of common elements