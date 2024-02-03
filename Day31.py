#Method and class declaration 
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        # Create an array to store the maximum sum at each index
        max_sum = [0] * len(arr)
        
        # Iterate through the array
        for i in range(len(arr)):
            # Initialize the current maximum value
            current_max = 0
            
            # Iterate from 1 to k or the remaining elements in the array, whichever is smaller
            for j in range(1, min(k, i + 1) + 1):
                # Update the current maximum value
                current_max = max(current_max, arr[i - j + 1])
                
                # Calculate the maximum sum and update the max_sum array
                max_sum[i] = max(max_sum[i], (max_sum[i - j] if i - j >= 0 else 0) + current_max * j)
        
        # The last element of max_sum array contains the maximum sum
        return max_sum[-1]
