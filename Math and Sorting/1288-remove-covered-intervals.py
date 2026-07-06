'''Description: Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.'''

'''Approach: First, let us sort by largest intervals first by modifying python's built-in sort function. While the sort function is running, we transform the Ends of the intervals into -End so they are able to get sorted in a descending order. Now, for a group of intervals with the
same starting point, the largest interval will come first. The starting points are ascending and the ending points are descending. Now,
we take the smallest possible ending point (say -1) as maxright and compare it with each end of our intervals. If the current interval's end is greater, we add it to our remaining count and update the maxright variable continue. If the current right is less than maxright, it is 
automatically absorbed into our intervals and hence we do not need to count it. 
Finally, we return the number of remaining intervals.
'''

class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        maxright = -1

        remaining = 0

        for left, right in intervals:
            if right > maxright:
                remaining += 1

                maxright = right

        return remaining


# Time Complexity: O(nlogn) due to python's built in sort
# Space Complexity: O(1)