#Description:There are several cards arranged in a row, and each card has an associated number of points.
# The points are given in the integer array cardPoints. In one step, you can take one card from the
# beginning or from the end of the row. You have to take  exactly k cards. Your score is the sum of the
# points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

#Approach Description: Let us take K cards from the left. Now, let us iterate from the right of the array,
#removing one element from the left and adding one from the right, until all K elements are from the right.
#Finally, return the maximum score found.

class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        total = sum(cardPoints[:k])

        maxPoints = total

        for i in range(k):

            total -= cardPoints[k - 1 - i]

            total += cardPoints[n - 1 - i]

            maxPoints = max(maxPoints, total)

        return maxPoints

#Time Complexity: O(k)
#Space complexity: O(1) for constant variable