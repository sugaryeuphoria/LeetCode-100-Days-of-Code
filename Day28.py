"""You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 """
#Class defintion
class Solution(object):
    #Method deinition
    def divideArray(self, nums, k):
       # Sort the array in ascending order
        nums.sort()

        # Initialize an empty array to store the result
        result = []

         # Iterate through the sorted array with a step size of 3
        for i in range(0, len(nums), 3):
             # Check if the difference between the third and first elements is greater than k
            if nums[i + 2] - nums[i] > k:
                return []  # If the condition is not satisfied, return an empty array