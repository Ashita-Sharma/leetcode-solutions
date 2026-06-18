#Description: Given an array of integers nums, sort the array in ascending order and return it.
#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and
#with the smallest space complexity possible.

#Approach: Although we can use Quick Sort, in some cases it can result in having more than nlogn time
#complexity, hence we use merge sort, which is always nlogn complexity. For this, we need two functions,
#merge and merge sort. Merge sort uses a divide and conquer tactic. It divides an array in half, applies
#merge sort on those two halves and then merges them back together.
#Hence, the lowest case ends up being where both halves have one member each and are merged.
#For the merging process, we take two pointers left and right, left traverses through left half and right
#traverses through right half. We initialize an empty array, in which we append the smallest element
#we find. Then we simply copy over the elements from the temp array to our final array.
#Note: The while condition in merging occurs when one half is exhausted but the other half still has
#elements remaining.

class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        # Merge both sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted temp into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Recursive merge sort
    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

#Time Complexity; O(nlogn)
#Space Complexity: O(n)
