#Description: You are given an integer array prices where prices[i] is the price of the ith item in a shop.
#Return an integer array answer where answer[i] is the final price you will pay for the ith item of
#the shop, considering the special discount.

#Approach 2: We start by creating an empty stack and duplicated our inital array. If the element is larger
#than the top, push its index onto the stack. If it's smaller, pop the top index, subtract that index's price
#with the current index's price  to get the discounted price. Do the same until we have gotten all prices.
#For the remaining items without a discount, they are in the resul list already so we do not have to
#do anything.

class Solution:
    def finalPrices(self, prices):
        res = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                res[idx] -= prices[i]

            stack.append(i)

        return res

#Time Complexity: O(n)
#Space complexity: O(n)