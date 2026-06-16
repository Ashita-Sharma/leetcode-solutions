#Description: Given the head of a singly linked list, group all the nodes with odd indices together
#followed by the nodes with even indices, and return the reordered list.
#The first node is considered odd, and the second node is even, and so on.
#Note that the relative order inside both the even and odd groups should remain as it was in the input.
#You must solve the problem in O(1) extra space complexity and O(n) time complexity.

#Approach: We initialize two pointers, odd and even. We mark odd as the head and even as the node after
#the head. We mark even's head as head's next. Now, while both even and odd exist, we let the odd node
#point to the node after even and even node to point to the 2nd node after it. We repeat this until we
#reach the end of the list. Then, we connect the last node of odd to the first node of even and return.

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head  # Connect odd list to even list
        return head

#Time Complexity: O(n)
#Space complexity: O(1)