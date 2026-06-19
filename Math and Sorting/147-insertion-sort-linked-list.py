#Description: Given the head of a singly linked list, sort the list using insertion sort, and
#return the sorted list's head.

#Approach: There are two cases possible. 1) The insertion happens inside the list.
# 2) Current element is smaller than the head itself. For the second case, we need to create a dummy node
#with the smallest possible size to point to the actual head. We keep track of the last sorted element as
#well, to mark the boundary between the sorted and unsorted portion.
#First, we take the first element from the unsorted region (last_sorted.next) and see where it fits in
#the list. If it is greater than, or equal to the last sorted value, we can mark it as sorted and label
#it as the last sorted and move on to the next element. Otherwise, we start from the dummy head, checking
#which element's val is greater than our current element's and insert it there.

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy_head = ListNode(val=-5000, next=head)
        last_sorted = head
        curr = head.next
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # Search for the position to insert
                prev = dummy_head
                while prev.next.val <= curr.val:
                    prev = prev.next

                # Insert
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = last_sorted.next

        return dummy_head.next

#Time Complexity: O(n^2)
#Space complexity: O(1)