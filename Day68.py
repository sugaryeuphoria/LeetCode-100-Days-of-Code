"""
3005. Count Elements With Maximum Frequency
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
# Method and class definition
class Solution(object):
    def maxFrequencyElements(self, nums):
                kMax = 100  # Define the maximum possible value in nums
                ans = 0  # Initialize the answer to 0
                count = [0] * (kMax + 1)  # Initialize a list of zeros with length kMax + 1 to count the frequencies
                 # Count the frequency of each number in nums
                for num in nums:
                    count[num] += 1  # Increment the count of the current number
                    maxFreq = max(count)  # Find the maximum frequency
 # Add the maximum frequency to the answer for each frequency that equals the maximum frequency
                for freq in count:
                    if freq == maxFreq:  # If the current frequency equals the maximum frequency
                        ans += maxFreq  # Add the maximum frequency to the answer
                        return ans  # Return the answer

