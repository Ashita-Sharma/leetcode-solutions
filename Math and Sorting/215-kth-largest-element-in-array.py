#Description: Given an integer array nums and an integer k, return the kth largest element in
# the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

#Approach: We create a heap of k elements. If the current element is grater than the smallest element
#in the heap, we push it onto the heap. Whichever, element is at the lowest position at the
#end of the iteration is also the kth largest element.


class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]

#Time Complexity: O(nlogn) due to heap
#Space complexity: O(k)