#Description: Given an array of distinct integers arr, find all pairs of elements with the
#minimum absolute difference of any two elements.
#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr

#Approach: We sort the array for easy traversal, since the smallest difference will always be the
#difference between the current element and the element just after/before it. We initialize an empty list
#to store our answer. We consider the minimum difference to be infinity. While we traverse through
#the list, we add any pair that has difference equal to the minimum difference. If the difference is less
#than the minimum difference, we reset the result list and add the new pair to it.

class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        n = len(arr)
        res = []
        for i in range(n-1):
            if abs(arr[i]-arr[i+1]) == min_diff:
                res.append([arr[i], arr[i+1]])
            elif abs(arr[i]-arr[i+1]) < min_diff:
                res = []
                res.append([arr[i], arr[i+1] ])
                min_diff = abs(arr[i]-arr[i+1])
        return res

#Time Complexity: O(nlogn) due to sorting
#Space complexity: O(1)