#Description: You are given two integer arrays nums1 and nums2 sorted in non-decreasing order
#and an integer k. Define a pair (u, v) which consists of one element from the first array and one
#element from the second array. Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

#Approach: Imagine a matrix of nums1 and nums2 where the value at [i,j] is the sum of ith element of nums1
#and the jth element of nums2. Then, we find the smallest possible sums in first iteration (0,0),(1,0) and
# (2,0) and so on, which are the minimum possible first sums, and push them onto a minimum heap.
#As the heap automatically identifies the minimum value, we pop it and add it to our final list.
#Next, Supposing we took from (0,0), we move onto the next item in row 0 which is (0,1), push it to the heap.
#and repeat until we have our required amount of pairs.

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        res = []
        heap = []

        for i in range(min(m, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(res) < k:
            curr_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res


#Time Complexity: O(k(log(min(m,k))) due to heap
#Space complexity: O(min(m,k))