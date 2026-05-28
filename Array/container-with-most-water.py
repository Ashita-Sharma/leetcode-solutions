#Description: You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains
# the most water.

#Approach Description: Here, we can use sliding window to calculate the distance between the two lines
#Which can be taken as right-left, and the height of the container which will be the minimum of the two values
#at the current indices. By initializing the maximum capacity as 0, we can find the largest container.

class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

#Time Complexity: O(n)
#Space complexity: O(1) for constant variable