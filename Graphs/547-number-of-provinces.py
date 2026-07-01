'''Description: There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.'''

'''Approach: We maintain a set of provinces we have visited so far. We create a helper function that will check and add
new cities to  our set. We iterate through all cities in the range isConnected, and if the current city is not in visited,
we do a dfs and increment our provinces count.'''


class Solution:
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in visited:
                    dfs(cur)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces

#Time Complexity: O(N)
#Space complexity: O(N)
