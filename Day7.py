#class definition
class Solution(object):
    #method definition
    def removeDuplicates(self, nums):
        # Check if the list is empty
        if not nums:
            return 0
        
        # Initialize the unique element count
        unique_count = 1
        
        # Iteration through List: for i in range(1, len(nums)): -
        # This loop iterates through the list, starting from the second element (index 1) 
        # because the uniqueness of the first element is already known.
        for i in range(1, len(nums)):
            # Compare the current element with the previous one
            if nums[i] != nums[i - 1]:
                # If they are different, increment the unique count
                unique_count += 1
                # Update the current position with the unique element
                nums[unique_count - 1] = nums[i]
        
        # Return the count of unique elements
        return unique_count
