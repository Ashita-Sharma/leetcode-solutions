#Description:You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the
# nodes of the first two lists. Return the head of the merged linked list.

#Approach Description: Here, we can apply the concept of merge sort. First we can begin by initializing
#two pointers at the start of list 1 and 2. We compare the values and make the smallest one the head of
#our final list. We then increment that list's pointer by 1 and compare again, making the tail end of our
#final list point to the next smallest value and so on until we reach the end of the lists.

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next

#Time Complexity: O(m+n)
#Space complexity: O(1) as we are only rearranging the nodes rather than create new data