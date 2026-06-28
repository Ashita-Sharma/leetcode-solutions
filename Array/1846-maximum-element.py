'''You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:

The value of the first element in arr must be 1.
The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of arr to a smaller positive integer.
Rearrange the elements of arr to be in any order.
Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.'''


'''Approach: Since we have full freedom to rearrange the array, let us first sort it in an ascending order.
Now, we iterate over the array, reducing any numbers greater than the limit via the minimum function.
Finally, we return the last element(also the largest).'''

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        n = len(arr)

        arr[0] = 1
        for i in range(1, n):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]

#Time Complexity: O(nlogn) due to sorting
#Space complexity: O(1)