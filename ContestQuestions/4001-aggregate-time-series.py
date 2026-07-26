'''Description: You are given two 2D integer arrays series1 and series2.

Each element in both series is of the form [timestamp, value], where:

timestamp is an integer representing the time.
value is an integer representing the value at that timestamp.
Each array is sorted in strictly increasing order of timestamp.

For any timestamp not present in a series, its value is taken from the next available timestamp in the same series if one exists. Otherwise, its value is considered 0.

The aggregated series is formed by summing the corresponding values from both series at every timestamp that appears in either series.

Return the aggregated series as a 2D integer array of [timestamp, summedValue] pairs, sorted in strictly increasing order of timestamp.

An array is strictly increasing if each element is strictly greater than the previous element.'''

'''Approach: There are only 4 possible cases that can occur hence we only need to consider them. 
A) Both series have not reached the end: Find the minimum timestamp and aggregate the values, appending to the result array.
B) Series1 has finished but Series2 has not: Minimum is the timestamp of Series2 and its value, append to result.
C) Series2 has finished but Series1 has not: Minimum is the timestamp of Series1 and its value, append to result.
D) Both Series have finished: End the while loop and return the result.'''

class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        res = []
        i = 0
        j = 0
        n1 = len(series1)
        n2 = len(series2)

        while i < n1 or j < n2:
            if i == n1:
                curr = series2[j][0]
            elif j == n2:
                curr = series1[i][0]
            else:
                curr = min(series1[i][0], series2[j][0])

            val1 = series1[i][1] if i < n1 else 0
            val2 = series2[j][1] if j < n2 else 0

            res.append([curr, val1 + val2])

            if i < n1 and series1[i][0] == curr:
                i += 1

            if j < n2 and series2[j][0] == curr:
                j += 1

        return res

#Time complexity:O(n+m), where n is length of series1 and m is length of series2
#Space complexity: O(1), no extra space required