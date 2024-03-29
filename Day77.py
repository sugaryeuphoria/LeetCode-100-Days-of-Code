"""
57. Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
class Solution:
    def insert(self, intervals, newInterval):
        # Initialize an empty list to store the result
        result = []  
        # Initialize a flag to track whether the new interval has been inserted
        inserted = False  
         # Iterate through each interval in the given intervals list
        for interval in intervals: 
             # If the end of the current interval is before the start of the new interval
            if interval[1] < newInterval[0]: 
                # Append the current interval to the result list
                result.append(interval) 
                 # If the start of the current interval is after the end of the new interval 
            elif interval[0] > newInterval[1]: 
                # Check if the new interval has not been inserted yet
                if not inserted:  
                     # Append the new interval to the result list
                    result.append(newInterval) 
                    # Set the inserted flag to True
                    inserted = True  
                    # Append the current interval to the result list
                result.append(interval)  
                # If there is an overlap between the current interval and the new interval
            else: 
                  # Update the start of the new interval
                newInterval[0] = min(newInterval[0], interval[0]) 
                # Update the end of the new interval
                newInterval[1] = max(newInterval[1], interval[1])  
                # If the new interval has not been inserted yet
        if not inserted:  
             # Append the new interval to the result list
            result.append(newInterval) 
            # Return the result list containing merged intervals
        return result  




