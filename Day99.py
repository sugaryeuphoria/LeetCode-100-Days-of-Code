"""
1700. Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively.
All students stand in a queue. Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the 
stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the
front of the queue). Return the number of students that are unable to eat.

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

Constraints:

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
"""
class Solution(object):
    def countStudents(self, students, sandwiches):
      
        # Initialize counters for each preference
        preference_count = [0, 0] # [square, circular]
        
        # Count the number of each preference
        for student in students:
            preference_count[student] += 1
        
        # Loop through sandwiches until no student can eat
        for sandwich in sandwiches:
            if preference_count[sandwich] == 0:
                break  # No more students can eat, exit loop
            
            # Find the next student who prefers the current sandwich
            while students and students[0] != sandwich:
                # Rotate students until a match is found
                students.append(students.pop(0))
            
            # If no match found after rotating, no more students can eat
            if students[0] != sandwich:
                break
            
            # Remove the student who ate and update preference count
            students.pop(0)
            preference_count[sandwich] -= 1
        
        # Return the count of students who couldn't eat
        return len(students)
