"""
2073. Time Needed to Buy Tickets
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line 
(which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.

Constraints:
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
"""
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        # Get the total number of people in the queue
        n = len(tickets)
        # Calculate the total number of tickets needed to be bought
        total_tickets = sum(tickets)
        # Initialize the variable to track the total time taken
        time_taken = 0
        # Continue looping until all tickets are bought
        while total_tickets > 0:
            # Determine the number of tickets to buy for the person at position k
            buy_count = min(tickets[k], total_tickets)
            # Update the total time taken by the number of tickets bought
            time_taken += buy_count
            # Update the total number of tickets left to buy
            total_tickets -= buy_count
            # Reduce the number of tickets for the person at position k
            tickets[k] -= buy_count
            # Move to the next person in the queue (circular queue)
            k = (k + 1) % n

            # Return the total time taken to buy all tickets
        return time_taken
    
# Example usage:
solution = Solution()
print(solution.timeRequiredToBuy([2, 3, 2], 2))  # Output: 6
print(solution.timeRequiredToBuy([5, 1, 1, 1], 0))  # Output: 8

