#Description: Given an array of integers heights representing the histogram's bar height where the
#width of each bar is 1, return the area of the largest rectangle in the histogram.

#Approach: Initialize an empty list and stack for result and temp stack respectively.
#Algorithm - While iterating through the elements, if an element's value is greater tha stack's top, append
#it to the stack, otherwise pop the top element, with current element being labeled as right and the top of
#the stack as left. Calculate the area by (right - left - 1)*(height of popped element).
#Compare with current maximum, and update accordingly.

#Note: I added a 0 at the end of the heights list so the algorithm would not break and automatically
#Calculate rest of the areas as well for convenience.
#Also, left boundary should be taken as -1 if stack empty  to prevent index out of range error.

class Solution:
    def largestRectangleArea(self, heights):
        res = []
        stack = []
        max_area = 0
        heights.append(0)
        for x in range(len(heights)):
            while stack and heights[x] < heights[stack[-1]]:
                right = x
                curr = stack.pop()
                left = stack[-1] if stack else -1
                area = heights[curr]*(right - left - 1)
                max_area = max(area, max_area)
            stack.append(x)

        return max_area

#Time Complexity: O(n)
#Space complexity: O(n)