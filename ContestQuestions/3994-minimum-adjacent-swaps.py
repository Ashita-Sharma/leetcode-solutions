'''Description: You are given an integer array nums and two integers a and b such that a < b.

An array is called good if it can be split into three contiguous parts, in this order, such that:

Every element in the first part is less than a.
Every element in the second part is in the range [a, b] inclusive.
Every element in the third part is greater than b.
Any of the three parts may be empty.

In one adjacent swap, you may swap two neighboring elements of nums.

Return the minimum number of adjacent swaps required to make nums good. Since the answer may be very large, return it modulo 109 + 7.'''

'''Approach: Since the given constraints include 1 <= nums.length <= 10^5, it is best to create a solution that is 
of O(nlogn) time or lower. In this question, the order of the numbers does not matter, only the appropriate partitions matter.
Hence, we can simply label all numbers as either Green, Yellow or Red. If a number is less than a, it is marked with a 'G',
if it is greater than b, it is marked with an R and otherwise it is marked with a Y. For the optimal solution, we will always
shift all the greens, then the yellows and thus, reds will be automatically in the correct position. For ease of understanding,
we can consider the elements to be jumping over each other. For the green, it will jump over yellow and reds before them but not other 
greens, since their relative order does not matter. The yellows will jump over all the reds before them but not the greens as
they would already be in their correct positions. Finally, red is already in the correct position. Hence, we shall traverse
the array from left to right (after having replaced all numbers with G, Y and R), and keep track of yellows_seen and reds_seen.
Everytime we encounter a green, it has to jump over all previous reds and yellows, hence their frequency will be added to the answer.
If the current element is yellow, we increment yellows_seen, and add reds_seen to our answer. If we encounter a red, we simply
increment reds_seen. Thus, we can easily get our answer in linear time.'''

class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 +7
        for i in range(len(nums)):
            if nums[i] < a:
                nums[i] = "G"
            elif nums[i] > b:
                nums[i] = "R"
            else:
                nums[i] = "Y"

        ans = 0
        reds_seen = 0
        yellows_seen = 0
        for color in nums:
            if color == "R":
                reds_seen += 1
            elif color == "Y":
                yellows_seen += 1
                ans += reds_seen
            else:
                ans += reds_seen
                ans += yellows_seen
        return ans % MOD

#Time Complexity: O(n)
#Space complexity: O(1)