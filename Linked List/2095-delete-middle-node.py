#Description: You are given the head of a linked list. Delete the middle node, and return the
# head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
# where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

#Approach: We use the tortoise and the hare algorithm again. Fast moves two steps and slow moves one. When
#the fast reaches the end, the slow one will be at the node just before the middle. Then we simply move
#the slow's pointer to point to the node right after the middle.

class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        # Initialize slow pointer to head
        slow = head

        # Initialize fast pointer two steps ahead
        fast = head.next.next

        # Traverse until fast reaches end
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Bypass the middle node
        slow.next = slow.next.next

        # Return head of updated list
        return head

#Time Complexity: O(n)
#Space complexity: O(1)