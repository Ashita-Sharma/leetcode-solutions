#Description:Given a linked list, swap every two adjacent nodes and return its head. You must solve
#the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#Approach Description: Before we begin swapping, we shall store the next pair node so that upon swapping,
#the link between the pairs is not broken. Hence, at one time we look at 3 nodes at once.
#We start by swapping the first and second nodes i.e the second node now points to the first.
#But right now, the first also point's to the second, hence we change the first node to point to the next pair node.
#And then we move on to the next pair and so on until the end of the linked list.

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = npn
            prev.next = second

            prev = cur
            cur = npn

        return dummy.next

#Time Complexity: O(n)
#Space Complexity: O(1)