#Description: In a linked list of size n, where n is even, the ith node (0-indexed) of the linked
#list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

#Approach: We deply the tortoise and hare algorithm in this problem. The fast pointer moves by two and the
#slow pointer moves by 1. When fast reaches the end, slow reaches the middle. We shall also simultaneously
#reverse the first half. For that we will swap the slow pointer to point to the previous node,
#the previous node to become slow and slow to be swapped by its original next value.
#After exiting the loop, we shall add the first half node and second half node together, update the maximum,
#until we reach the end of the lists.

class Solution:
    def pairSum(self, head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next #swapping all three

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev, slow = prev.next, slow.next

        return res

#Time Complexity: O(n)
#Space Complexity: O(1)