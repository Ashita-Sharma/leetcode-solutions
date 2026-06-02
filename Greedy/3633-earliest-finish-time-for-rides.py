# You are given two categories of theme park attractions: land rides and water rides.
# A tourist must experience exactly one ride from each category, in either order.
# Return the earliest possible time at which the tourist can finish both rides.

#Approach Description: Let us start by initializing variables. Now, we can find the minimum time for the entirety
#of the land ride, i.e. the land ride with the minimum total time (start + duration) taken by iterating through
#all the values(first n loop). Next, we shall find the Land to Water schedule and calculate it's minimum
# time. (second m loop). Then, we shall find if the Water to Land schedule has a shorter total time than our
# current minimum (last loop). Finally, we return our answer.

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        minL = 3000
        minW = minL
        res = minL
        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            minL = min(minL, landStartTime[i] + landDuration[i])

        for i in range(m):
            minW = min(minW, waterStartTime[i] +  waterDuration[i])
            res = min(res, max(minL, waterStartTime[i]) +  waterDuration[i])

        for i in range(n):
            res = min(res, max(minW, landStartTime[i]) + landDuration[i])

        return res

#Time Complexity: O(n+m)
#Space complexity: O(1)