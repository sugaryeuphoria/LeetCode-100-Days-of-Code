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

             # Iterate through the elements before the current element
            for j in range(i):  

                 # If the current element is divisible by the previous element
                if nums[i] % nums[j] == 0:  

                      # Update the length of the subset
                    dp[i] = max(dp[i], dp[j] + 1) 

                    # If the updated length is greater than the maximum length, update the maximum length and its index
                    if dp[i] > max_length:  
                        max_length = dp[i]  
                        max_index = i  

                        # Initialize an empty list to store the result
        result = []  

           # Initialize a variable to track the current length
        curr_length = max_length  

        # Iterate backwards from the maximum index to 0
        for i in range(max_index, -1, -1): 

             # If the current length matches the length in dp and either max_index divides nums[i] or nums[i] divides max_index
            if curr_length == dp[i] and (max_index % nums[i] == 0 or nums[i] % max_index == 0):  

                 # Add the current number to the result
                result.append(nums[i])  

                  # Decrease the current length
                curr_length -= 1  

                 # Return the result in reverse order
        return result[::-1] 