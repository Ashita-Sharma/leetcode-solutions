#Description: Given an unsorted integer array nums. Return the smallest positive integer that is not
#present in nums. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

#Approach Description: Let us iterate once to mark any numbers greater than n and make the fit the range.
#Then, let us mark indices of seen numbers like question 448, by turning their corresponding index negative.
#Next, iterate through one last time and when we find a number greater than 0, we know it's index is the number
#that we haven't seen, thus we can immediately break the loop and return the answer.

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            x = abs(nums[i])

            if 1 <= x <= n:
                idx = x - 1

                if nums[idx] > 0:
                    nums[idx] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1



#Time Complexity: O(n)
#Space complexity: O(1)