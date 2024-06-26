"""
786. K-th Smallest Prime Fraction
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2
"""
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        # Get the length of the array
        n = len(arr)
        # Initialize the answer array with [0, 1]
        ans = [0, 1]
        # Set the initial left boundary of the search space
        l = 0
        # Set the initial right boundary of the search space
        r = 1

        # Start binary search
        while True:
            # Calculate the midpoint of the current interval
            m = (l + r) / 2
            # Reset the numerator of the answer fraction
            ans[0] = 0
            # Initialize a counter for the number of fractions less than or equal to the current guess
            count = 0
            # Initialize the second pointer
            j = 0

            # Iterate through the array
            for i in range(n):
                # Move the second pointer until the fraction satisfies the condition
                while j < n and arr[i] >= m * arr[j]:
                    j += 1
                # Count the number of fractions less than or equal to the current guess
                count += n - j
                # Update the answer fraction if needed
                if j < n and ans[0] * arr[j] < ans[1] * arr[i]:
                    ans[0] = arr[i]
                    ans[1] = arr[j]

            # Update the boundaries of the search space based on the count
            if count < k:
                l = m
            elif count > k:
                r = m
            else:
                return ans  # Return the answer if kth fraction is found
