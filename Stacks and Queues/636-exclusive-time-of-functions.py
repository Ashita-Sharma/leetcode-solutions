#Description: On a single-threaded CPU, we execute a program containing n functions. Each function
#has a unique ID between 0 and n - 1. Return the exclusive time of each function in an array, where the
#value at the ith index represents the exclusive time for the function with ID i.

#Approach Description: It is important to remember that the functions are exclusive, i.e. their runtimes
#do not overlap. Hence, we can push the "start" functions into the stack, with the time for the topmost
#function being current_time - start_time. However, for the deeper functions, when a new function is pushed,
#we modify the function's total time to be its start_time - func 2's start_time, and THEN we update the stack
#and the current time. When the deeper function finally ends, we add (prev_time - current_time) to it's total
#time. All times are stored according to their respective index and id.

class Solution:
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func_id, typ, timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_time

                stack.append(func_id)
                prev_time = timestamp

            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return ans

#Time Complexity: O(m), where m is length of logs
#Space complexity: O(n), because of stack
