#Class declaration
class Solution(object):
    #Method declaration 
    def removeElement(self, nums, val):
       # Check if the list is empty
        if not nums:
             # If empty, no elements to remove, return 0

            return 0 
        # Initialize a pointer for non-val elements
        non_val_pointer = 0

        # Iterate through the list
        for i in range(len(nums)):
            # Check if the current element is not equal to val
            if nums[i] != val:
                # Update the non-val element at the pointer position
                nums[non_val_pointer] = nums[i]
                # Move the pointer to the next position
                non_val_pointer += 1

        # Return the count of non-val elements
        return non_val_pointer
