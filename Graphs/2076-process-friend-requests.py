'''You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.

Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.

A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.

Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is n.'''

"""Approach: For the given constraints, although not recommended, a brute force method is also possible. We can simply
maintain a list for all current friendships. If a restriction member is found in the list, we can simply check them and
block the request from processing. Alternatively, the optimal approach is to use DSU and maintain a representative 
for each friend group. Hence, instead of checking lists we can just see if the current friend request has the same parent
as the restriction and process the friend requests in that manner."""


class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu, ans = DSU(n), []
        for x, y in requests:
            x_p, y_p = dsu.find(x), dsu.find(y)
            bad = True
            for a, b in restrictions:
                a_p, b_p = dsu.find(a), dsu.find(b)
                if set([a_p, b_p]) == set([x_p, y_p]):
                    bad = False
                    break

            ans += [bad]
            if bad: dsu.union(x, y)

        return ans

#Time complexity: O(n * m * log(n)
#Space complexityL O(n)