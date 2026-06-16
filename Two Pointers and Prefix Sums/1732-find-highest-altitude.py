#Description:There is a biker going on a road trip. The road trip consists of n + 1
#points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
#You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
#i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

#Approach: We take two variables altitude sum and maximum sum. We iterate through all elements in the
#array, adding them to the sum and updating the maximum. Then, we return the final result.

class Solution:
    def largestAltitude(self, gain):
        alt_sum = 0
        max_alt = 0
        for alt in range(len(gain)):
            alt_sum += gain[alt]
            max_alt = max(alt_sum, max_alt)
        return max_alt

#Time Complexity: O(n)
#Space complexity: O(1)
