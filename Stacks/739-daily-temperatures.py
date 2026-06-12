#Description: Given an array of integers temperatures represents the daily temperatures, return an
#array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer
#temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

#Approach Description: Create a resultant array of only 0s that is the length of the provided array.
#Initialize an empty stack to place the indices in. Now, iterating through all indices in temperatures.
#If a temperature is less than the temperature of top of the stack, push its index onto the stack. Otherwise,
#pop the top index and modify the resulting index to have the value of the difference between the days, i.e.
#Current index - Top Index. Finally, return the resulting array.

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                res[x] = i - x
            stack.append(i)

        return res

#Time Complexity: O(n)
#Space complexity: O(n)