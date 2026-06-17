#Description: Given an array of intervals where intervals[i] = [starti, endi], merge all
#overlapping intervals, and return an array of the non-overlapping intervals that cover all the
#intervals in the input.

#Approach: Iterate through all items in the sorted list, if the start of the current element is less
#than the end of the last element of result, then we update that element of result. Otherwise, we make it
#the next element of result.

class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res

#Time Complexity: O(nlogn)
#Space complexity: O(1)