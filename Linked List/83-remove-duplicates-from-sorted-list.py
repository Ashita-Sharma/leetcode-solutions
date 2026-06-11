#Description: Given the head of a sorted linked list, delete all duplicates such
#that each element appears only once. Return the linked list sorted as well.

#Approach Description: We start from the beginning for the linked list, storing the current node as head and checking
#if the next node's value is equal to the current. If it is, make the current node point to the node after it's next
#node(say, second node). Repeat until we reach end of the list.

class Solution:
    def deleteDuplicates(self, head):
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res

#Time Complexity: O(n)
#Space complexity: O(1)