#Desccription: There are n people in a line queuing to buy tickets, where the 0th person is at the
#front of the line and the (n - 1)th person is at the back of the line.
#You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith
#person would like to buy is tickets[i].
#Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

#Approach 1: While the list still exists, decrease the first person's count by 1. If their count is 0,
#pop them out entirely. Otherwise, return them to the back. Meanwhile, after each iteration we decrease the
#index of k by one. If k becomes -1, we mark it to the end of the list and repeat until we get our answer.

class Solution1:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        while tickets:
            time += 1
            tickets[0] -= 1

            if tickets[k] == 0:
                return time

            elif k != 0 and tickets[0] == 0:
                tickets.pop(0)
                k -= 1
                if k == -1:
                    k = len(tickets) - 1
            else:
                left = tickets.pop(0)
                tickets.append(left)
                k -= 1
                if k == -1:
                    k = len(tickets) - 1


#Approach 2: The core algorithm stays the same, but we create a nested list that will keep the value of
#tickets[i] as well as its original index. Now we can repeat the same algorithm without worrying about
#keeping track of index k.

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        for i in range(len(tickets)):
            tickets[i] = [tickets[i], i]

        while tickets:
            time += 1
            tickets[0][0] -= 1

            if tickets[0][1] == k and tickets[0][0] == 0:
                return time

            elif tickets[0][1] != k and tickets[0][0] == 0:
                tickets.pop(0)

            else:
                left = tickets.pop(0)
                tickets.append(left)

#Time Complexity: O(n*m) where n is length of list and m is number of tickets k needs to buy
#Space complexity: O(1) for both approach