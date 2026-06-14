#Description: You are given an array target of n integers. From a starting array arr
# consisting of n 1's, you may perform the following procedure :
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to x.
# You may repeat this procedure as many times as needed.
# Return true if it is possible to construct the target array from arr, otherwise, return false.

#Approach: First, let us consider this- In the target array, the largest number will always be the sum
#Of the other two numbers. Hence, we can use that to loop through, going back from target until we reach our
#original array of only 1's.
#We create a max heap that will hold all target values. Next, we shall pop the largest element, and
#Calculate the sum of the remaining elements. Since the array only contains numbers greater than one,
# It is impossible for the remaining sum to be 0. If the remaining sum is greater than the max sum, it is
#impossible to get the highest value. Hence, we return false. We repeat this until we have reached the
#end of the heap.


class Solution:
    def isPossible(self, target):
        sm = sum(target)
        heap = []

        for x in target:
            heappush(heap, -x)

        while -heap[0] > 1:
            mx = -heappop(heap)
            rest_sm = sm - mx

            if rest_sm == 1:
                return True

            if rest_sm == 0:
                return False

            prev_mx = mx % rest_sm
            if prev_mx == 0 or prev_mx >= mx:
                return False

            heappush(heap, -prev_mx)
            sm = rest_sm + prev_mx

        return True

#Time Complexity: O(nlogn) due to heap
#Space complexity: O(n)