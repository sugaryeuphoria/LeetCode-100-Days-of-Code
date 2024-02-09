"""Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
"""
#Class definition
class Solution(object): 

     # Define a function to find the largest divisible subset
    def largestDivisibleSubset(self, nums):  

         # If nums is empty, return an empty list
        if not nums:  
            return [] 
        
         # Sort the input list
        nums.sort()  

        # Get the length of the input list
        n = len(nums)  
        
        # Initialize a dynamic programming array with all elements set to 1
        dp = [1] * n

         # Initialize variables to track the maximum length and its index
        max_length = 1  
        max_index = 0  

          # Iterate through the elements of the input list
        for i in range(1, n): 