"""
514. Freedom Trail
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.

Example 1:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Example 2:

Input: ring = "godding", key = "godding"
Output: 13

Constraints:

1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict
        
        # Create a dictionary to store the index positions of each character in the ring
        char_index = defaultdict(list)
        for i, char in enumerate(ring):
            char_index[char].append(i)
        
        # Create a memoization dictionary to store the minimum steps required to spell the substring starting from index i with the ring at position j
        memo = {}
        
        # Helper function to calculate the minimum steps
        def dp(i, j):
            if i == len(key):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            min_steps = float('inf')
            for index in char_index[key[i]]:
                # Calculate the steps needed to rotate the ring to position index
                steps = abs(j - index)
                steps = min(steps, len(ring) - steps)  # Choose the minimum steps considering both clockwise and anticlockwise rotations
                
                # Recursively calculate the minimum steps for the next character in key
                next_steps = dp(i + 1, index)
                
                # Total steps required is the steps to rotate to the current character + steps required for the next characters
                min_steps = min(min_steps, steps + next_steps + 1)  # Add 1 for pressing the center button
                
            memo[(i, j)] = min_steps
            return min_steps
        
        # Start from the first character in key and the initial position of the ring
        return dp(0, 0)

# Test cases
solution = Solution()
print(solution.findRotateSteps("godding", "gd"))  # Output: 4
print(solution.findRotateSteps("godding", "godding"))  # Output: 13
