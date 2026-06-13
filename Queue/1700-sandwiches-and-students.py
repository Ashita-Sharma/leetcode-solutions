#Description: The school cafeteria offers circular and square sandwiches at lunch break, referred to
#by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or
#circular sandwiches. The number of sandwiches in the cafeteria is equal to the number of students.
#The sandwiches are placed in a stack. At each step:
# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it
# and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

#Approach Description: We create a variable containing the amount of total students. If a student gets their
#preferred sandwich, they and their sandwich are removed from the arrays and the count is reduced by 1.
#If a student does not get their preferred sandwich, they are popped from the queue and join the end.
#If the current sandwich is not preferred by ANY student, the loop ends and the number of students left is
#returned.


class Solution:
    def countStudents(self, students, sandwiches):
        students_left = len(sandwiches)
        while students:
            if sandwiches[0] not in students:
                return students_left

            elif students[0] == sandwiches[0]:
                students_left -= 1
                students.pop(0)
                sandwiches.pop(0)

            elif students[0] != sandwiches[0]:
                left = students.pop(0)
                students.append(left)

        return students_left


#Time Complexity: O(n)
#Space complexity: O(1)