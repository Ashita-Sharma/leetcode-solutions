'''You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.'''

'''Approach: The question asks us to find the minimum edge weight for any two points in ***a*** path from 1 to n. 
That means we do not need to find the path with the minimum number of nodes or the minimum total weight but just the 
smallest possible weight that can come in a path between 1 and n. For this, let us create a list of all relations 
between each city and their associated weights. Now, from city 1, we will calculate the minimum distance to all other
cities. The cities not yet visited will be added to our queue, then we shall traverse their paths and update our minimum
as we go along. As we are only exploring paths indirectly or directly connected to 1 and n, any path between them with
the minimum edge weight will automatically be valid. Hence, we can easily return the minimum.'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = [False] * (n + 1)

        queue = deque([1])
        visited[1] = True

        answer = float("inf")

        while queue:
            city = queue.popleft()

            for next_city, distance in graph[city]:
                answer = min(answer, distance)

                if not visited[next_city]:
                    visited[next_city] = True
                    queue.append(next_city)

        return answer

# Time Complexity: O(V + E)
# Space Complexity: O(V)