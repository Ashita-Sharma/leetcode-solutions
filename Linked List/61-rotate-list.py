#Description: Given the head of a linked list, rotate the list to the right by k places.

#Approach Description: The remainder of k with respect to length of the list is the amount of times we have
#to rotate the list. To rotate the list, we unlink the list from the start to k-1 node and attach it to the last node.
#then we return the k-th node as head.

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1

        position = k % length
        if position == 0:
            return head

        current = head

        for _ in range(length - position - 1):
            current = current.next

        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head

# Time complexity: O(n)
# Space complexity: O(1)