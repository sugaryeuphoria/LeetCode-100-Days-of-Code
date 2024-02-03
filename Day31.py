#Method and class declaration 
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        # Create an array to store the maximum sum at each index
        max_sum = [0] * len(arr)
        
       