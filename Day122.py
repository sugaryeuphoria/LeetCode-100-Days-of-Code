"""
881. Boats to Save People
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        # Sort people in ascending order
        people.sort()
        # Initialize pointers
        left, right = 0, len(people) - 1
        # Initialize boat count
        boats = 0
        # Iterate until left pointer crosses right pointer
        while left <= right:
            # Check if two heaviest people can fit in the boat
            if people[left] + people[right] <= limit:
                # Move left pointer to next person
                left += 1
                # Always move right pointer to next person, as one person will be in the boat
                right -= 1
                # Increment boat count
                boats += 1
        
        return boats