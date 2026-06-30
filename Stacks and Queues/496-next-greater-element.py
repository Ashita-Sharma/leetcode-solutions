'''Description: The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above. '''

'''Approach: We are told that nums1 is a subset of nums2. So, we start by taking the first num in nums2, and checking
if the element after it is greater. If not, we push it onto the stack, keep it on hold. If we do find a number immediately
 to the right that is greater than the current element, we add the pair to a dictionary, popping said element. Then, we
 take the next top element in stack and repeat until we can no longer. We repeat this for all numbers in nums2.
 Now, we have the values mapped in the dctionary as [nums1]->[nums2], hence we can easily create a list using num for 
 numbers in nums 1, keeping the mapped num2 in their place in the resultant string. If it doesn't have a map in the
 dictionary, we return -1.'''


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mp = defaultdict(lambda: -1)
        st = []

        for num in nums2:
            while st and st[-1] < num:
                mp[st.pop()] = num
            st.append(num)

        return [mp[num] for num in nums1]

#Time Complexity: O(m+n)
#Space complexity: O(m), because of stack and dictionary
