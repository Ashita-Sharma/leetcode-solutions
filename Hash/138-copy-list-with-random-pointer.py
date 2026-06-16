#Description: A linked list of length n is given such that each node contains an additional random
#pointer, which could point to any node in the list, or null.
#Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where
#each new node has its value set to the value of its corresponding original node. Both the next and random
#pointer of the new nodes should point to new nodes in the copied list such that the pointers in the
#original list and copied list represent the same list state. None of the pointers in the new list should
#point to nodes in the original list.

#Approach: We first iterate through all the nodes to create its mapping with the new nodes. Next, we
#iterate through the old nodes again, using the hash map to mark the new node's next and random by using
#the old nodes' next and random hash values. Finally, we return the new head.


class Solution:
    def copyRandomList(self, head):
        if not head:

            return None
        node = head
        mp = {}
        while node:
            mp[node] = Node(node.val)
            node = node.next

        curr = head
        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next
        return mp[head]

#Time Complexity: O(n)
#Space complexity: O(n)for the dictionary