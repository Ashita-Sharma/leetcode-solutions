#Description: You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list.

#Approach Description: We shall begin from the leftmost node, i.e. the ones places,
#adding the two numbers together and keeping their remainder by 10 in the new node and saving the carry-over.
#Then we move on to the next two nodes and so on until we reach the end of the list.

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

#Time Complexity: O(n), where n is the size of longer list.
#Space complexity: O(n) due to the creation of the new list