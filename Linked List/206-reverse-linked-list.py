#Description: Given the head of a singly linked list, reverse the list, and return the reversed list.

#Approach: When we try to reverse a linked list, we need to store 3 variables at once. The current node,
#the previous node and the next node. When we reach a node, we store its next node's value in Front,
#and its previous node's value in prev. Now, we point curr node to previous, and label the previous node
#as current, since they have now swapped places. Previous becomes the current node and the current node
#becomes the one after it, i.e. we move forward by one node. We do this until current becomes none and
#return the new head.

class Solution:
    def reverseList(self, head):
        # Initialize previous pointer to None
        prev = None

        # Start from the head of the list
        temp = head

        # Traverse the list
        while temp:
            # Save the next node
            front = temp.next

            # Reverse the current node's pointer
            temp.next = prev

            # Move prev to current node
            prev = temp

            # Move to the next node
            temp = front

        # Return new head (last node becomes first)
        return prev

#Time Complexity: O(n)
#Space complexity: O(1)