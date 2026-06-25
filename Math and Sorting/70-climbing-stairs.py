# Description; You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Approach: First, let us consider the three base cases. For n = 1, there is only one way to climb the
# stairs, for n = 2 there is two (1,1 and 2 steps) and for n = 3 there are three (1,1,1 1,2 and 2,1).
# Now, let us consider the smallest possible case, n = 4. For n = 4, we can either take one step from 3 or
# 2 steps from 2. Similarly for 5, we can either take one step from 4 or two steps from 3. Hence, for any
# number n, we only need to know the amount of ways to reach the last and second to last step. The total
# cases for number n will be the sum of the two. Then, for n+1, the second to last value will be for n-1
# and the last will be n, and we can calculate it from that and so on.

class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n

        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur


#Time Complexity: O(n)
#Space complexity: O(1)