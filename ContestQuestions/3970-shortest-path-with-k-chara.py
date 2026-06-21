# Description: You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
#
# You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.
#
# Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

#Approach: First similar to 3965 problem, we make a structure to store all relations, but not just the
#pair of nodes but their assigned weights as well. Now, we use Dijkstra's algorithm by using heap function.
#We start with the zero(th) node and work our way down to the node n-1. In the heap, we also keep track of
#how many consecutive characters we've seen so far. For each neighbouring node of our current element,
#we calculate how many total consecutive characters we've seen so far. If we get more than k consecutive
#characters, we skip that node since it is not valid. If we encounter a new character, we reset our chara
#counter to zero. Either way, we push the new nodes onto our heap. Since, it is a min-heap, we
#automatically select the shortest valid path. For each node we pop, we keep the total distance in a
#variable. Finally, when we reach the n-1 node, we return the total distance. Otherwise, if traverse
#all the nodes without reaching n-1 node (example: due to consecutive character constraints) we return -1.

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges, labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        heap = [(0, 0, 1)]

        dist = {}

        while heap:
            d, u, cnt = heappop(heap)

            if (u, cnt) in dist:
                continue

            dist[(u, cnt)] = d

            if u == n - 1:
                return d

            for v, w in graph[u]:

                if labels[v] == labels[u]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                if (v, new_cnt) not in dist:
                    heappush(heap, (d + w, v, new_cnt))

        return -1


#Time Complexity: O(nlogn) due to heap
#Space complexity: O(n)