# Description: You want to build n new buildings in a city. The new buildings will be built
# in a line and are labeled from 1 to n.
# However, there are city restrictions on the heights of the new buildings:
# The height of each building must be a non-negative integer.
# The height of the first building must be 0.
# The height difference between any two adjacent buildings cannot exceed 1.
# Additionally, there are city restrictions on the maximum height of specific buildings.
# These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti]
# indicates that building idi must have a height less than or equal to maxHeighti.
# It is guaranteed that each building will appear at most once in restrictions, and building 1 will not
# be in restrictions. Return the maximum possible height of the tallest building.

#Approach: Whenever we reach a position for a new building, given that we can only increase each height by
#one, we have no choice but to always chose the minimum height from either the restriction or the height
#based on the neighbouring buildings. So, we do one pass by taking restrictions from the left side,
#Then we take the minimum from the left restrictions and the right restrictions.
#Finally, having received the minimum heights of all buildings, we get the maximum height from the
#restrictions. However, the height can still extend towards the right after the final restriction.
#Hence, we take the maximum of restricted height and height of last building.

class Solution:
    def maxBuilding(self, n: int, restrictions):
        restrictions.append([1, 0])
        restrictions.sort()
        m = len(restrictions)

        def yCap(x1, y1, x2, y2):
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            return (y1 + y2 + x2 - x1) >> 1

        for i in range(1, m):
            restrictions[i][1] = yCap(*restrictions[i - 1], *restrictions[i])

        for i in range(m - 2, -1, -1):
            restrictions[i][1] = yCap(*restrictions[i + 1], *restrictions[i])

        res = 0
        for i in range(1, m):
            res = max(res, yPeak(*restrictions[i - 1], *restrictions[i]))

        return max(res, restrictions[-1][1] + n - restrictions[-1][0])

#Time Complexity: O(mlogm) where m is the length od the restrictions array
#Space complexity: O(m)