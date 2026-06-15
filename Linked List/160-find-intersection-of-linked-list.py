# Given the heads of two singly linked-lists headA and headB, return the node at which the two
# lists intersect. If the two linked lists have no intersection at all, return null.

#Approach: We can connect list B at the end of list A and list A at the end of list B.
#Then, if both lists DO intersect, then they will reach a common node. Otherwise, they will never
#reach the same node.

class Solution:
    def getIntersectionNode(self, headA, headB):
        lista = headA
        listb = headB

        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA

        return listb

#Time Complexity: O(n+m)
#Space complexity: O(1)