#Class declaration
class Solution(object):
    #Method declaration 
    def removeElement(self, nums, val):
       # Check if the list is empty
        if not nums:
            return 0  # If empty, no elements to remove, return 0

        # Initialize a pointer for non-val elements
        non_val_pointer = 0

