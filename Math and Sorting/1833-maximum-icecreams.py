#Description: It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.
#
# Note: The boy can buy the ice cream bars in any order.
#
# Return the maximum number of ice cream bars the boy can buy with coins coins.
#
# You must solve the problem by counting sort.

#Approach: Assuming we have a sorted array, the process is quite simple. We simply iterate in ascending
#order, increasing our count of icecreams by 1 every time we meet an icecream we can afford and reduce the
#total coins by the cost. However, if we cannot afford the current icecream, we also wouldn't be able to
#buy the other icecreams as they are arranged in ascending order. Hence, we break the loop and return
#our answer. The main topic is counting sort, which is required by the problem statement.
#Counting sort includes creating a list of the frequencies of each element, where index is the element
#value and index's element is the frequency. Simultaneously, we also calculate its cumulative sum and
#store it in the frequency array. Then, we move in reverse, taking element at index i of the original array
#to be the index of the frequency array and use its frequency value - 1 to find the index at which the
#element at index[i] of the original array must be kept. We decrement that element's corresponding
#frequency by 1. We repeat this in reverse order until we get all the elements sorted.


class Solution:
    def maxIceCream(self, costs, coins):
        if not costs:
            return 0

        n = len(costs)
        maxval = max(costs)

        cntArr = [0] * (maxval + 1)

        for v in costs:
            cntArr[v] += 1

        for i in range(1, maxval + 1):
            cntArr[i] += cntArr[i - 1]

        ans = [0] * n
        for i in range(n - 1, -1, -1):
            v = costs[i]
            ans[cntArr[v] - 1] = v
            cntArr[v] -= 1

        count = 0
        for cost in ans:
            if cost <= coins:
                count +=1
                coins -= cost
            else:
                return count
        return count

#Time Complexity: O(n+m) where n is size of original array and m is size of frequency array
#Space complexity: O(n+m)