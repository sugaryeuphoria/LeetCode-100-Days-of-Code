"""
621. Task Scheduler
You are given an array of CPU tasks, each represented by letters A to Z,
and a cooling time, n. Each cycle or interval allows the completion of one task.
Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by
at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B.
In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as
2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads
to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        # Step 1: Count the frequency of each task
        freq = Counter(tasks)
        # Step 2: Sort the tasks based on their frequencies
        sorted_tasks = sorted(freq.values(), reverse=True)
        # Step 3: Calculate the maximum frequency
        max_freq = sorted_tasks[0]
        # Step 4: Determine the number of idle slots required
        idle_slots = (max_freq - 1) * n
        # Step 5: Iterate through the sorted tasks
        for task in sorted_tasks[1:]:
            idle_slots -= min(task, max_freq - 1)
            # Step 6: Calculate the minimum intervals required
        idle_slots = max(0, idle_slots)  # Ensure idle_slots is non-negative
        return len(tasks) + idle_slots
    
solution = Solution()
print(solution.leastInterval(["A","A","A","B","B","B"], 2))  # Output: 8
print(solution.leastInterval(["A","C","A","B","D","B"], 1))  # Output: 6
print(solution.leastInterval(["A","A","A","B","B","B"], 3))  # Output: 10




