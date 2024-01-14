#class definition
class Solution(object):
    #method definition
    def removeDuplicates(self, nums):
        # Check if the list is empty
        if not nums:
            return 0
        
        # Initialize the unique element count
        unique_count = 1
        
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # Compare the current element with the previous one
            if nums[i] != nums[i - 1]:
            