# Descriptions: Given an integer array nums, return the number of reverse pairs in the array.
#
# A reverse pair is a pair (i, j) where:
#
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].

#Approach: We use merge sort to make our calculations easier. First, we start the merge sort normally but
#before we merge tge two halves, we run a loop to compare each element from the left with each element from
#the right to count the number of reverse pairs. Then we merge normally. Finally, we return the count.
#This reduces the time complexity from O(n^2) to O(nlogn)

class Solution:
    def reversePairs(self, nums):
        count = 0

        def merge(arr, low, mid, high):
            temp = []
            left, right = low, mid + 1

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def mergeSort(arr, low, high):
            nonlocal count

            if low >= high:
                return

            mid = (low + high) // 2

            mergeSort(arr, low, mid)
            mergeSort(arr, mid + 1, high)

            j = mid + 1

            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1

                count += j - (mid + 1)

            merge(arr, low, mid, high)

        mergeSort(nums, 0, len(nums) - 1)

        return count

#Time Complexity: O(nlogn)
#Space complexity: O(n)