# Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

#Approach: Suppose we have a list that forms a cycle. So when one pointer enters the cycle, it will continue
#moving in a cycle until we forcibly stop it. Here, we can use the tortoise and the hare algorithm. The hare
#moves by 2, and enters the cycle first. The slower tortoise starts later and joins the cycle late. The
#hare jumps by 2 and hence will reach a point where both of them are at the same spot. If that happens, we
#know a cycle exists, hence we return True. If fast reaches null, we know we've reached the end and return
#False.

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

#Time Complexity: O(n)
#Space complexity: O(1)