"""Two Sum : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"""

#Class definition
class Solution(object):

    #method definition
    def twoSum(self, nums, target):
        
        #empty dictionary to store indexes
        indx_dict = {}


        #Loop throught the list as for loop iterates over the element of nums where i is the index and num is current element
        for i,num in enumerate(nums):

            #Calculate the complement needed to reach target
            num_to_reach_target = target-num

            #Check if complement is already in indx_dict
            if  num_to_reach_target in indx_dict:
                return [indx_dict[ num_to_reach_target],i]
            
             #if complement is not in dictionary it adds current num to its index place 
            indx_dict[num]=i


           