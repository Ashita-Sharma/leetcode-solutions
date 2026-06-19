#Description: You are given an integer mountain array arr of length n where the values increase to a
#peak element and then decrease.
#Return the index of the peak element.
#Your task is to solve it in O(log(n)) time complexity.

#Approach: We use the classic binary search approach. Find the middle of the array. If the element after
#middle is greater than the middle element, we know our peak lies on the right, so we discard the left
#and repeat until we find peak. Otherwise, we move to the left side. If we do not find any peak, we know
#our old middle was the answer, hence we return low.

class Solution:
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr) -1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low
#Time Complexity; O(1logn)
#Space Complexity: O(1)