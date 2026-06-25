# Description: You are given an integer array nums and an integer target.
# Return the number of subarrays of nums in which target is the majority element.
# The majority element of a subarray is the element that appears strictly more than half of the times in
# that subarray.

#Approach: We only need to check if the target is the median. For this, we have no explicit use for any
#other numbers, hence we do not have to care about their values, only care about target's value.
#Here, instead of a dictionary we use an array map for convenience. We maintain the balance of the subarray
#by +1 for every target we see and -1 for every non-target number we see. We take presum as the number of
#valid subarrays at this point. If the current number is a target, we get more valid subarrays, but if the
#next element is not the target, the balance is shifted and number of valid subarrays decrease.
#At the end of each number visited, we update the answer with presum.

class Solution:
    def countMajoritySubarrays(self, nums, target):
            n = len(nums)

            pre = [0] * (2 * n + 1)

            pre[n] = 1

            cnt = n
            presum = 0
            ans = 0

            for x in nums:
                if x == target:
                    presum += pre[cnt]

                    cnt += 1
                    pre[cnt] += 1
                else:
                    cnt -= 1

                    presum -= pre[cnt]
                    pre[cnt] += 1

                ans += presum

            return ans

#Time Complexity: O(n)
#Space complexity: O(n) for the hash array