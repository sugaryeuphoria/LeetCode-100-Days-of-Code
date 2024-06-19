"""
1482. Minimum Number of Days to Make m Bouquets
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
"""
class Solution(object):
    def minDays(self, bloomDay, m, k):
        # Helper function to check if we can make m bouquets by `day`
        def canMakeBouquets(day):
            # Initialize the number of bouquets and the current count of adjacent flowers
            bouquets = 0
            flowers = 0
            # Iterate through each bloom day in the bloomDay array
            for bloom in bloomDay:
                # If the current flower blooms by the given day
                if bloom <= day:
                    flowers += 1  # Increment the count of adjacent flowers
                     # If we have enough flowers to make a bouquet
                    if flowers == k:
                        bouquets += 1  # Increment the count of bouquets
                        flowers = 0  # Reset the count of adjacent flowers
                else:
                    flowers = 0  # Reset the count of adjacent flowers if the current one hasn't bloomed
                    # If we have already made enough bouquets
                if bouquets >= m:
                    return True  # Return True as it's possible to make m bouquets
                return False  # Return False if we can't make m bouquets
             # If the total number of flowers needed is more than available, return -1
        if m * k > len(bloomDay):
            return -1
         # Initialize the binary search range
        left, right = min(bloomDay), max(bloomDay)
         # Perform binary search
        while left < right:
            mid = (left + right) // 2  # Compute the mid point
            if canMakeBouquets(mid):  # If we can make m bouquets by mid day
