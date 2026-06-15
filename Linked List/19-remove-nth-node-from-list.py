#Description: Given the head of a linked list, remove the nth node from the end of the list and
#return its head.

#Approach: We keep a result node that points to the head. Now, we know that if the list has a length L,
#the nth node from the end will be at L-nth node from the start. Hence, we can employ the tortoise and
#hare algorithm again. We keep one pointer at nth position from the start and one at the head node.
#Now, we move both one at a time. When the pointer reaches end, the other pointer would've reached
#L-nth node from the start. Then, we can let it skip the nth node and point to the node after it.

class Solution:
    def removeNthFromEnd(self, head, n):
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next

#Time Complexity: O(N) where N is the length of the list
#Space complexity: O(1)