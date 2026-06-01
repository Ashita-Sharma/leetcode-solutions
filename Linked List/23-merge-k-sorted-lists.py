#Description:You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

#Approach Description: Let us use a minimum heap structure to find the minimum value from the k heads
#of the linked lists. Then, we mark the minimum one as the head (popping it) and push its next node onto the heap
#We then call heapify to make it a valid MinHeap again, and repeat until all nodes have been utilized.

class Solution:
    def mergeKLists(self, lists):
        minHeap = []
        for node in lists:
            while node:
                minHeap.append(node.val)
                node = node.next
        heapq.heapify(minHeap)

        head = current = ListNode(-1)
        while minHeap:
            current.next = ListNode(heapq.heappop(minHeap))
            current = current.next

        return head.next

#Time Complexity: O(nlogk), based on number of nodes and lists
#Space complexity: O(k), based on number of lists