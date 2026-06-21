# Description: You are given an integer array lights of length n, representing positions 0 through n - 1 on a road.
#
# For each position i:
#
# If lights[i] = v, where v > 0, there is a working bulb at position i that illuminates every position from max(0, i - v) to min(n - 1, i + v), inclusive.
# If lights[i] = 0, there is no working bulb at position i.
# A position is visible if it is illuminated by at least one working bulb.
#
# You may install additional bulbs at any positions. Each additional bulb installed at position j illuminates positions from max(0, j - 1) to min(n - 1, j + 1), inclusive.
#
# Return the minimum number of additional bulbs required to make every position on the road visible.

#Approach: We need to find a way to mark the array inside itself to know if an element is "lit up" or not.
#For this, every time we see an element that has a functioning light bulb (v > 0), we mark the start of
#the illuminated area from the left by 1 and the first element with darkness from the right by -1.
#Now, we initialize an array named "visibles" that will keep track of every unlit element.
#We traverse through the lights array as well, taking the prefix sum of elements seen so far. If the sum is
#greater than zero, we know that we are currently in a "lit up" area and mark those elements' visibility as
#true. For our third and final pass, we first need to remember that every additional bulb is able to light
#up at most 3 bulbs, one to the left, one to the right and its own position. Hence, we keep a track of all
#the false we encounter in our visibles array. When we get a True. We calculate the bulbs needed and add it
#to our result, resetting our counter to zero. Finally, we return the result.

class Solution:
    def minLights(self, lights) -> int:
        visibles = [False]*len(lights)
        n = len(lights)
        min_bulb = 0
        diff = [0]*(n+1)
        for i, v in enumerate(lights):
            if v > 0:
                L = max(0, i-v)
                R = min(n-1, i+v)
                diff[L] += 1
                if R+1 < n:
                    diff[R+1] -= 1
            print(diff)
        count = 0
        curr = 0
        for i in range(n):
            curr += diff[i]
            visibles[i] = curr > 0
            print(visibles)
        for pos in range(len(visibles)):
            if not visibles[pos]:
                count += 1
            else:
                min_bulb += (count +2) // 3
                count = 0
        min_bulb += (count + 2) // 3
        return min_bulb

