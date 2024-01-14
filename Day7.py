#class definition
class Solution(object):
    #method definition
    def removeDuplicates(self, nums):
        # Check if the list is empty
        if not nums:
            return 0
        
        # Initialize the unique element count
        unique_count = 1
        
      