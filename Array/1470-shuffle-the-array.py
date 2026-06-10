#Description: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

#Approach Description: Create an array of size 2n. Then, for n, add the first element of both lists,
#then move on to the next and so on until having iterated through all elements.

class Solution:
    def shuffle(self, nums, n):
        ans = [0] * (2 * n)
        for i in range(2 * n):
            if i % 2 == 0:
                ans[i] = nums[i // 2]
            else:
                ans[i] = nums[n + i // 2]
        return ans

#Time Complexity: O(n)
#Space complexity: O(2n)